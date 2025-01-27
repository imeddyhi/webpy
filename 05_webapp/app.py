import web
urls = (
    '/', 'Index'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
    def POST(self):
        form = web.input()
        nombre = form.nombre
        email = form.email
        mensaje = form.mensaje
        response = "Hola " + nombre + ", tu email es " + email + " y tu mensaje es " + mensaje
        diccionario = {
            'nombre': nombre,
            'email': email,
            'mensaje': mensaje
        }
        return response, diccionario

if __name__ == "__main__":
    app.run() # Inicializa el servidor web