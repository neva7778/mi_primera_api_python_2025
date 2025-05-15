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

# URLs de nuestros endpoints Flask
url_flask_saludo_get = "http://127.0.0.1:5000/api/saludo"
url_flask_saludo_post = "http://127.0.0.1:5000/api/crear_saludo" # Nuevo endpoint

# URLs de nuestros endpoints FastAPI
url_fastapi_raiz = "http://127.0.0.1:8000/"
url_fastapi_item_get = "http://127.0.0.1:8000/items/42?q=consulta_desde_cliente"
url_fastapi_saludo_post = "http://127.0.0.1:8000/api/crear_saludo_fastapi" # Nuevo endpoint


"""try...except requests.exceptions.RequestException as e:: Es una buena
práctica envolver las solicitudes de red en un bloque try...except. Si el
servidor no está disponible o hay un problema de red, requests puede lanzar
una excepción. Esto evita que nuestro script cliente se bloquee.
"""

print("--- Probando API Flask ---")
try:
    response_flask_get = requests.get(url_flask_saludo_get)
    # Usamos la función requests.get() para realizar una solicitud HTTP GET a la URL especificada.
    # El resultado se almacena en la variable response_flask. Este es un objeto Response de la librería requests.
    
    response_flask_get.raise_for_status() # Lanza una excepción para códigos de error HTTP (4xx o 5xx)
    """Si la solicitud HTTP resultó en un código de estado de error del cliente (4xx) o del
    servidor (5xx), este método lanzará una excepción HTTPError. Si la solicitud fue exitosa
    (códigos 2xx), no hace nada. Es una forma rápida de verificar errores comunes.
    """

    datos_flask_get = response_flask_get.json() # Convierte la respuesta JSON a un diccionario Python
    """Si la respuesta del servidor contiene datos JSON válidos (y la cabecera Content-Type
    es application/json, lo cual Flask y FastAPI hacen por nosotros), este método automáticamente:
    - Lee el contenido del cuerpo de la respuesta.
    - Parsea (convierte) la cadena JSON en una estructura de datos de Python (generalmente un diccionario o una lista).
    """

    print(f"Respuesta de Flask (código {response_flask_get.status_code}):")
    """El objeto Response también tiene un atributo status_code que
    contiene el código de estado HTTP devuelto por el servidor
    (por ejemplo, 200 para OK, 404 para Not Found).
    """
    
    # Usamos json.dumps para una impresión más legible del JSON
    print(json.dumps(datos_flask_get, indent=2, ensure_ascii=False)) 
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


print("--- Probando API Flask (POST Crear Saludo) ---")
try:
    # Datos que vamos a enviar en el cuerpo de la solicitud POST
    datos_para_enviar_flask = {"nombre": "Ana Conda"} 

    # Hacemos la solicitud POST, enviando los datos como JSON
    # requests se encarga de establecer la cabecera Content-Type a application/json
    # Usamos requests.post() para realizar la solicitud POST
    response_flask_post = requests.post(url_flask_saludo_post, json=datos_para_enviar_flask)
    """json=datos_para_enviar_flask: Este es un parámetro muy conveniente
    de requests. Cuando le pasas un diccionario al parámetro json, requests
    automáticamente:
    -Convierte el diccionario Python a una cadena JSON.
    - Establece la cabecera HTTP Content-Type a application/json.
    - Coloca la cadena JSON en el cuerpo de la solicitud POST.
    """

    response_flask_post.raise_for_status() # Chequea errores HTTP

    datos_recibidos_flask = response_flask_post.json()
    print(f"Respuesta de Flask POST (código {response_flask_post.status_code}):")
    print(json.dumps(datos_recibidos_flask, indent=2, ensure_ascii=False))
    print("-" * 30)

except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la API de Flask (POST): {e}")
    print("-" * 30)


"""Hacemos lo mismo para los endpoints de FastAPI. 
ota que desde la perspectiva del cliente que usa requests,
¡la forma de interactuar con una API GET que devuelve JSON
es idéntica, ya sea que el backend esté hecho con Flask o FastAPI!
"""


print("--- Probando API FastAPI (Raíz GET) ---")
try:
    response_fastapi_raiz = requests.get(url_fastapi_raiz)
    response_fastapi_raiz.raise_for_status()
    datos_fastapi_raiz = response_fastapi_raiz.json()
    print(f"Respuesta de FastAPI Raíz GET (código {response_fastapi_raiz.status_code}):")
    print(json.dumps(datos_fastapi_raiz, indent=2, ensure_ascii=False))
    print("-" * 30)
except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la API de FastAPI (Raíz GET): {e}")
    print("-" * 30)

print("--- Probando API FastAPI (Item GET) ---")
try:
    response_fastapi_item = requests.get(url_fastapi_item_get)
    response_fastapi_item.raise_for_status()
    datos_fastapi_item = response_fastapi_item.json()
    print(f"Respuesta de FastAPI Item GET (código {response_fastapi_item.status_code}):")
    print(json.dumps(datos_fastapi_item, indent=2, ensure_ascii=False))
    print("-" * 30)
except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la API de FastAPI (Item GET): {e}")
    print("-" * 30)

print("--- Probando API FastAPI (POST Crear Saludo) ---")
try:
    # Datos correctos
    datos_para_enviar_fastapi_ok = {"nombre": "Barry Allen", "edad": 30}

    response_fastapi_post_ok = requests.post(url_fastapi_saludo_post, json=datos_para_enviar_fastapi_ok)
    response_fastapi_post_ok.raise_for_status()

    datos_recibidos_fastapi_ok = response_fastapi_post_ok.json()
    print(f"Respuesta de FastAPI POST OK (código {response_fastapi_post_ok.status_code}):")
    print(json.dumps(datos_recibidos_fastapi_ok, indent=2, ensure_ascii=False))
    print() # Salto de línea

    # Datos incorrectos (falta 'nombre', 'edad' es un string)
    datos_para_enviar_fastapi_error = {"apelido": "Wayne", "edad": "treinta y cinco"}

    print("Intentando enviar datos incorrectos a FastAPI POST...")
    response_fastapi_post_error = requests.post(url_fastapi_saludo_post, json=datos_para_enviar_fastapi_error)
    # NO usamos raise_for_status() aquí para poder ver el cuerpo del error 422

    print(f"Respuesta de FastAPI POST con error (código {response_fastapi_post_error.status_code}):")
    # El error 422 de FastAPI ya es JSON, así que lo imprimimos directamente
    print(json.dumps(response_fastapi_post_error.json(), indent=2, ensure_ascii=False))
    print("-" * 30)

except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP al conectar con la API de FastAPI (POST): {http_err}")
    try:
        error_details = http_err.response.json()
        print("Detalles del error (JSON):")
        print(json.dumps(error_details, indent=2, ensure_ascii=False))
    except json.JSONDecodeError:
        print(f"Detalles del error (texto): {http_err.response.text}")
    print("-" * 30)
except requests.exceptions.RequestException as req_err:
    print(f"Error de conexión con la API de FastAPI (POST): {req_err}")
    print("-" * 30)