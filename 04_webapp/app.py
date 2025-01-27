import web
urls = (
    '/', 'Index',
    '/bienvenida', 'Bienvenida'    
)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
class Bienvenida:
    def GET(self):
        return render.bienvenida()

if __name__ == "__main__":
    app.run()