from fastapi import FastAPI
from pydantic import BaseModel # Importamos BaseModel de Pydantic
from typing import Optional # Lo mantenemos por si lo usamos en otros lados

# 1. Crear una instancia de la aplicación FastAPI
app = FastAPI()


# Modelo Pydantic para los datos de entrada del saludo
# Esto define la "forma" o "esquema" de los datos que esperamos.
"""Todas las clases que definen esquemas de datos con Pydantic
deben heredar de BaseModel.
"""
class SaludoRequest(BaseModel):
    nombre: str
    edad: None | int = None # Hacemos la edad opcional


# 2. Definir una ruta y su función asociada
# FastAPI puede trabajar con funciones asíncronas (async def) y también con funciones normales (def).
"""
Esto es un decorador de operación de ruta (path operation decorator).
Le dice a FastAPI que la función que está debajo (hola_mundo_raiz) es la encargada de manejar las
solicitudes que lleguen a la ruta (path) / utilizando el método HTTP GET.
FastAPI tiene decoradores para todos los métodos HTTP estándar: @app.post(), @app.put(), @app.delete(),
@app.options(), @app.head(), @app.patch()."""
@app.get("/")  # Usamos el decorador @app.get() para definir una ruta del tipo GET
async def hola_mundo_raiz():
    return {"mensaje": "¡Hola, mundo desde FastAPI!"}

"""
Si devuelves un diccionario de Python, una lista, un modelo Pydantic
(lo veremos pronto), o incluso un solo valor como un string o int,
FastAPI lo convertirá automáticamente a una respuesta JSON. No necesitas
llamar a una función como jsonify de Flask explícitamente (aunque FastAPI
también tiene JSONResponse para casos más avanzados).
"""

"""
Aquí vemos async def en lugar de solo def. Esto define una corutina o función asíncrona.
Cuando esta función es llamada, no se ejecuta inmediatamente, sino que devuelve un objeto corutina.
Permite que un programa continúe ejecutando otras tareas mientras espera que se completen
operaciones largas (que no consumen CPU activamente, sino que esperan por algo externo
que es un tiempo de espera o "I/O-bound operation").
"""


"""
sync def en Python: Declara una función como una corutina. Cuando esta función es llamada,
no se ejecuta inmediatamente, sino que devuelve un objeto corutina.

await en Python: Se usa dentro de una función async def para pausar la ejecución
de la corutina actual y permitir que el programa ejecute otras tareas, hasta que
la operación "esperada" (awaitable) se complete. Típicamente se usa await con otras
funciones async def o con objetos que representan operaciones de I/O.

Beneficio en FastAPI: FastAPI puede usar async def para manejar rutas. Si tu
función de ruta necesita realizar operaciones que implican espera (como llamar
a otra API, acceder a una base de datos de forma asíncrona), puede usar await.
Mientras espera, FastAPI (a través del servidor ASGI) puede usar ese tiempo
para procesar otras solicitudes entrantes, mejorando enormemente el rendimiento
y la capacidad de manejar muchas conexiones concurrentes.

Importante: Para el "Hola Mundo" simple que solo devuelve un diccionario, usar
async def no ofrece una ventaja de rendimiento directa porque no hay ninguna
operación de await real (no estamos esperando nada). Sin embargo, es idiomático
en FastAPI mostrar que puede ser asíncrono, y es una buena práctica usar
async def para tus funciones de ruta si anticipas que podrían realizar operaciones
de I/O en el futuro o si quieres mantener la consistencia. FastAPI también maneja
funciones def síncronas de manera eficiente ejecutándolas en un pool de hilos
separado si es necesario.
"""

@app.get("/items/{item_id}")
async def leer_item(item_id: int, q: str | None = None):
    """
    Lee un item por su ID y opcionalmente un query string adicional.
    """
    # item_id se declara como int, FastAPI hará la conversión y validación.
    # q es un parámetro de consulta opcional de tipo string.
    # Python 3.10+ para 'str | None', para versiones anteriores usa 'Optional[str] = None' de 'typing'
    response = {"item_id": item_id}
    if q:
        response.update({"q": q}) # el tipado dinamico de Python permite esto
    return response

"""
{item_id} define una parte de la URL que será variable. El valor que se ponga
ahí será pasado como argumento a la función leer_item.
"""

"""
item_id: int: Esto es una anotación de tipo (type hint) de Python. Le decimos
a FastAPI que esperamos que item_id sea un entero (int). FastAPI usará esto para:
Convertir el valor de la ruta (que siempre llega como string) a un entero.
Validar que la conversión sea posible. Si visitas /items/foo, FastAPI 
automáticamente devolverá un error JSON indicando que "foo" no es un entero
válido. <!-- end list -->
Aquí empezamos a tocar la magia de Pydantic, aunque no lo hemos importado
directamente. FastAPI usa Pydantic bajo el capó para esta validación y
conversión basada en type hints.
"""

"""
q: str | None = None:
Esto define un parámetro de consulta (query parameter) opcional llamado q.
str | None: Significa que q puede ser una cadena de texto (str) o None
(si no se proporciona). En Python 3.9 o anterior, escribirías
Optional[str] = None (necesitarías from typing import Optional).
= None: Lo hace opcional. Si no se incluye ?q=valor en la URL,
q será None dentro de la función.
Ejemplo de URL: /items/5?q=mi-busqueda (aquí item_id es 5, q es "mi-busqueda")
Ejemplo de URL: /items/10 (aquí item_id es 10, q es None)
"""


# Nuevo endpoint para manejar POST con validación Pydantic
@app.post("/api/crear_saludo_fastapi", status_code=201) # Podemos definir el status_code por defecto aquí
async def api_crear_saludo_fastapi_post(datos_saludo: SaludoRequest):
     # 'datos_saludo' será una instancia de SaludoRequest.
    # FastAPI automáticamente:
    # 1. Lee el cuerpo de la solicitud.
    # 2. Valida que sea un JSON con los campos 'nombre' (str) y opcionalmente 'edad' (int).
    # 3. Si la validación falla, devuelve un error 422 Unprocessable Entity con detalles.
    # 4. Si la validación es exitosa, convierte los datos en una instancia de SaludoRequest.

    mensaje_respuesta = f"¡Hola, {datos_saludo.nombre}! Tu saludo ha sido procesado por FastAPI."
    if datos_saludo.edad is not None:
        mensaje_respuesta += f" Veo que tiene {datos_saludo.edad} años."
    
    respuesta = {
        "mensaje": mensaje_respuesta,
        "datos_recibidos": datos_saludo.model_dump()  # .dict() en Pydantic v1
    }
    return respuesta



# No necesitamos el bloque if __name__ == '__main__': app.run() aquí.
# La aplicación se ejecuta con un servidor ASGI como Uvicorn desde la terminal.

# Se ejecuta con el siguiente comando:
# uvicorn app_fastapi:app --reload
"""
uvicorn: Es el comando para iniciar el servidor Uvicorn.
app_fastapi:app:
app_fastapi: Es el nombre de tu archivo Python (sin el .py).
app: Es el nombre de la variable dentro de app_fastapi.py que
contiene tu instancia de FastAPI (recuerda: app = FastAPI()).
El : los separa.
--reload: Esta opción hace lo mismo que debug=True en Flask.
Uvicorn vigilará los cambios en tus archivos y reiniciará
el servidor automáticamente. 
"""

"""
ASGI es la evolución de WSGI para el mundo asíncrono. Es una
interfaz estándar que permite a los servidores web (como
Uvicorn, Daphne, Hypercorn) comunicarse con aplicaciones
Python que pueden ser asíncronas (usando async/await).
Uvicorn es un servidor ASGI. Actúa como el intermediario
entre las solicitudes de red entrantes y tu aplicación
FastAPI. Recibe la solicitud HTTP, la pasa a FastAPI en
un formato que ASGI define, FastAPI la procesa
(posiblemente de forma asíncrona), y devuelve una respuesta
que Uvicorn luego envía de vuelta al cliente.
Gracias a ASGI, Uvicorn y FastAPI pueden manejar
código asíncrono de manera nativa, lo que es clave para
el alto rendimiento de FastAPI. ASGI también permite manejar
otros protocolos además de HTTP, como WebSockets, en el mismo servidor.
Uvicorn puede servir aplicaciones sobre HTTP/1.1 y también
tiene soporte para HTTP/2, lo que puede ofrecer mejoras
adicionales de rendimiento sin que necesites cambiar
tu código de FastAPI.
"""
