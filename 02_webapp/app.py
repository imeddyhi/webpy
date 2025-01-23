import web
urls = (
    '/', 'Index'
    '/login', 'Login'    
    '/respuesta', 'Redspuesta'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
class Login:
    def GET(self):
        return render.authentication.login()
class Respuesta:
    def GET(self):
        respuesta = "Holiiii"
        return render.chat(respuesta)

if __name__ == "__main__":
    app.run()