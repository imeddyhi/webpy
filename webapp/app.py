import web # Carga la librería web.py

urls = (
    '/(.*)', 'Hello' # La clase hello atenderá las solicitudes desde la ruta raíz /
)
app = web.application(urls, globals()) #Aplicación web, se le pasa las rutas y variables para pasar parametros entre apps

class Hello:
    def GET(self, name): # self llama a la clase, name es un parametro que recibirá la app web
        if not name: # Si no recibe un nombre pondrá la variable name con 'World'
            name = 'World'
        return 'Hola, ' + name + '!'

if __name__ == "__main__":
    app.run() # Inicializa el servidor web