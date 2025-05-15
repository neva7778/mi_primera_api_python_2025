from flask import Flask, jsonify

"""
Hemos añadido jsonify a nuestra línea de importación. jsonify es una función
de Flask muy útil que toma un diccionario de Python (o una lista) y lo convierte
en una cadena con formato JSON. Además, y muy importante, configura correctamente
la cabecera HTTP Content-Type de la respuesta a application/json. Esto le dice al
cliente (navegador, script, etc.) que el contenido que está recibiendo es JSON.
"""

# 1. Crear una instancia de la aplicación Flask
app = Flask(__name__)

"""
El argumento __name__ es una variable especial de Python que contiene el nombre
del módulo actual. Flask lo usa para determinar la ruta raíz de la aplicación y
para encontrar recursos como plantillas y archivos estáticos. Para un script que
se ejecuta directamente, __name__ será "__main__".'''
"""


# 2. Definir una ruta y su función asociada
@app.route('/')     #Esta es la ruta raíz o principal de nuestro sitio web
def hola_mundo():
    return '¡Hola, mundo desde Flask!'

"""
En Flask, @app.route() se usa para asociar una URL (una ruta) con una función de
Python. Cuando alguien acceda a esa URL en su navegador, la función que está
debajo del decorador se ejecutará.

La ruta '/' representa la URL raíz de nuestro sitio web (por ejemplo, si tu
servidor se ejecuta en http://127.0.0.1:5000, entonces '/' corresponde
a http://127.0.0.1:5000/).
"""


# Nuevo endpoint o ruta que devuelve JSON
"""
Es una buena práctica común prefijar las rutas de tu API con /api/ para distinguirlas
de las rutas que podrían servir páginas web HTML tradicionales, aunque no es estrictamente
obligatorio.
"""
@app.route('/api/saludo')
def api_saludo():
    # Creamos un diccionario de Python
    mensaje = {
        "id": 1,
        "texto": "Hola desde mi primera API con Flask!",
        "lenguaje": "Python",
        "tipo": "JSON"
    }
    # Usamos jsonify para convertir el diccionario en un objeto JSON
    # y establecer la cabecera Content-Type a application/json
    return jsonify(mensaje)

"""
En lugar de devolver una simple cadena de texto como antes, ahora usamos jsonify(mensaje).
Flask tomará el diccionario mensaje, lo convertirá en una cadena JSON válida (por ejemplo,
{"id": 1, "texto": "¡Hola desde mi primera API con Flask!", ...}), y creará una respuesta
HTTP con esa cadena como cuerpo y la cabecera Content-Type establecida en application/json.
"""


# 3. (Opcional pero recomendado) Definir una función para ejecutar la aplicación
if __name__ == '__main__':
    # Ejecuta la aplicación Flask
    # debug=True permite la recarga automática y proporciona un depurador en el navegador
    # (reinicia el servidor automáticamente al detectar cambios en el código y muestra errores detallados)
    app.run(debug=True)

"""
Esta es una construcción estándar en Python. El código dentro de este bloque solo
se ejecutará si el script (app_flask.py) se ejecuta directamente (por ejemplo,
python app_flask.py), y no si se importa como un módulo en otro script.

mportante: El servidor de desarrollo de Flask (app.run()) es excelente para el
desarrollo local, pero no es adecuado para producción (cuando tu aplicación está
disponible para el público en internet). Para producción, se usan servidores WSGI
más robustos como Gunicorn o uWSGI.

Este servidor de desarrollo de Flask, por defecto, utiliza el
protocolo HTTP/1.1.
"""
