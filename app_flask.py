from flask import Flask

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
