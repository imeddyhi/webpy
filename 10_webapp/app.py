import web
import requests
import json

# URL de la base de datos Firebase
FIREBASE_URI = "https://eddydemo-f3fa8-default-rtdb.firebaseio.com/usuarios.json"

# Estructura de las rutas en la aplicación web
urls = (
    '/', 'Index',
    '/bienvenida', 'Bienvenida'
)

# Plantilla para renderizar las vistas
app = web.application(urls, globals())
render = web.template.render('views', base='master')

class Index:
    def GET(self):
        # Mostrar el formulario de inicio de sesión
        return render.index()

    def POST(self):
        # Obtener los datos ingresados por el usuario
        user_data = web.input()
        nombre = user_data.nombre
        email = user_data.email
        password = user_data.password

        # Realizar la petición GET a Firebase para obtener los datos de los usuarios
        response = requests.get(FIREBASE_URI)

        if response.status_code == 200:
            usuarios = response.json()
            # Verificar si el usuario existe en la base de datos
            for key, usuario in usuarios.items():
                if (usuario.get("nombre") == nombre and 
                    usuario.get("email") == email and 
                    usuario.get("password") == password):
                    # Redirigir a la página de bienvenida si las credenciales son correctas
                    web.seeother(f'/bienvenida?nombre={nombre}')
            return render.error("Usuario, correo o contraseña incorrectos.")
        else:
            return render.error("Error al conectar con la base de datos Firebase.")

class Bienvenida:
    def GET(self):
        # Obtener el nombre del usuario pasado en la URL
        user_data = web.input(nombre="")
        return render.bienvenida(user_data.nombre)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
