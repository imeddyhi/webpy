import web

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        # Mostrar el formulario de la calculadora
        return render.index(result=None)

    def POST(self):
        # Procesar los datos enviados desde el formulario
        data = web.input()
        try:
            first_number = float(data.first_number)
            second_number = float(data.second_number)
            operation = data.operation

            if operation == '+':
                result = first_number + second_number
            elif operation == '-':
                result = first_number - second_number
            elif operation == '*':
                result = first_number * second_number
            elif operation == '/':
                result = first_number / second_number if second_number != 0 else "Error: División por cero"
            else:
                result = "Operación no válida"
        except ValueError:
            result = "Por favor ingrese números válidos"

        # Renderizar el resultado en la página
        return render.index(result=result)

if __name__ == "__main__":
    app.run()
