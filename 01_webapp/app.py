import web # Carga la librería web.py

urls = (
    '/', 'Hello', # La clase hello atenderá las solicitudes desde la ruta raíz /
    '/bye', 'Bye'
)
app = web.application(urls, globals()) #Aplicación web, se le pasa las rutas y variables para pasar parametros entre apps

class Hello:
    def GET(self): # self llama a la clase
        return 'Hola, web.py!'

class Bye:
    def GET(self): # self llama a la clase
        return 'Bye, web.py!'

if __name__ == "__main__":
    app.run() # Inicializa el servidor web