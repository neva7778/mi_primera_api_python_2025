import requests # Importa la librería que acabamos de instalar.
import json

"""Importamos el módulo json estándar de Python. Lo usaremos
con json.dumps() para "imprimir bonito" el JSON
(con indentación), lo cual es opcional pero útil para la legibilidad.
"""

# URLs de nuestros endpoints
"""Definimos las URLs completas de los endpoints que creamos en
nuestros servidores Flask y FastAPI.
"""
url_flask_saludo = "http://127.0.0.1:5000/api/saludo"
url_fastapi_raiz = "http://127.0.0.1:8000/"
url_fastapi_item = "http://127.0.0.1:8000/items/42?q=consulta_desde_cliente"


"""try...except requests.exceptions.RequestException as e:: Es una buena
práctica envolver las solicitudes de red en un bloque try...except. Si el
servidor no está disponible o hay un problema de red, requests puede lanzar
una excepción. Esto evita que nuestro script cliente se bloquee.
"""

print("--- Probando API Flask ---")
try:
    response_flask = requests.get(url_flask_saludo)
    # Usamos la función requests.get() para realizar una solicitud HTTP GET a la URL especificada.
    # El resultado se almacena en la variable response_flask. Este es un objeto Response de la librería requests.
    
    response_flask.raise_for_status() # Lanza una excepción para códigos de error HTTP (4xx o 5xx)
    """Si la solicitud HTTP resultó en un código de estado de error del cliente (4xx) o del
    servidor (5xx), este método lanzará una excepción HTTPError. Si la solicitud fue exitosa
    (códigos 2xx), no hace nada. Es una forma rápida de verificar errores comunes.
    """

    datos_flask = response_flask.json() # Convierte la respuesta JSON a un diccionario Python
    """Si la respuesta del servidor contiene datos JSON válidos (y la cabecera Content-Type
    es application/json, lo cual Flask y FastAPI hacen por nosotros), este método automáticamente:
    - Lee el contenido del cuerpo de la respuesta.
    - Parsea (convierte) la cadena JSON en una estructura de datos de Python (generalmente un diccionario o una lista).
    """

    print(f"Respuesta de Flask (código {response_flask.status_code}):")
    """El objeto Response también tiene un atributo status_code que
    contiene el código de estado HTTP devuelto por el servidor
    (por ejemplo, 200 para OK, 404 para Not Found).
    """
    
    # Usamos json.dumps para una impresión más legible del JSON
    print(json.dumps(datos_flask, indent=2, ensure_ascii=False)) 
    """json.dumps() toma un objeto Python (como nuestro diccionario
    datos_flask) y lo convierte de nuevo en una cadena con formato JSON.
    - indent=2: Le dice a dumps que indente la salida JSON con 2 espacios,
    haciéndola mucho más legible.
    - ensure_ascii=False: Permite que caracteres no ASCII
    (como la ¡ en nuestro saludo) se muestren directamente en lugar
    de secuencias de escape Unicode (como \u00a1),
    asumiendo que tu terminal soporta UTF-8.
    """

    print("-" * 30)

except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la API de Flask: {e}")
    print("-" * 30)


"""Hacemos lo mismo para los endpoints de FastAPI. 
ota que desde la perspectiva del cliente que usa requests,
¡la forma de interactuar con una API GET que devuelve JSON
es idéntica, ya sea que el backend esté hecho con Flask o FastAPI!
"""

print("--- Probando API FastAPI (Raíz) ---")
try:
    response_fastapi_raiz = requests.get(url_fastapi_raiz)
    response_fastapi_raiz.raise_for_status()

    datos_fastapi_raiz = response_fastapi_raiz.json()
    print(f"Respuesta de FastAPI Raíz (código {response_fastapi_raiz.status_code}):")
    print(json.dumps(datos_fastapi_raiz, indent=2, ensure_ascii=False))
    print("-" * 30)

except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la API de FastAPI (Raíz): {e}")
    print("-" * 30)

print("--- Probando API FastAPI (Item) ---")
try:
    response_fastapi_item = requests.get(url_fastapi_item)
    response_fastapi_item.raise_for_status()

    datos_fastapi_item = response_fastapi_item.json()
    print(f"Respuesta de FastAPI Item (código {response_fastapi_item.status_code}):")
    print(json.dumps(datos_fastapi_item, indent=2, ensure_ascii=False))
    print("-" * 30)

except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la API de FastAPI (Item): {e}")
    print("-" * 30)

