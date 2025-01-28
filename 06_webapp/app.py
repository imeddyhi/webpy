import web
urls = (
    '/', 'Index'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
        for i in range(5):
            print(i)
        for o in range(6):
            if o == 2:
                continue
            elif o == 3:
                print('TRES')
            else:
                print(i)

if __name__ == "__main__":
    app.run() # Inicializa el servidor web