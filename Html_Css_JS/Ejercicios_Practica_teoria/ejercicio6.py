from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def visual():
    return render_template("Ejercicio_6.html")

@app.route("/numeros", methods = ['GET', 'POST'])
def pag_operacion():
    if request.method == 'GET':
        numero_1 = int(request.args.get("numero_1"))
        numero_2 = int(request.args.get("numero_2"))
        operacion = request.args.get("operacion")
        
        mensaje = f'<h1>Los numeros son:  {numero_1} y {numero_2} y la operacion es: {operacion}</h1> <br>'
        
        if operacion == "Suma":
            return f'{mensaje} <h2>El resultado es:  {numero_1 + numero_2}'
        elif operacion == "Resta":
            return f'{mensaje} <h2>El resultado es:  {numero_1 - numero_2}'
        elif operacion == "Multiplicacion":
            return f'{mensaje} <h2>El resultado es:  {numero_1 * numero_2}'
        else :
            return f'{mensaje} <h2>El resultado es:  {numero_1 / numero_2}'

if __name__ == "__main__":
    app.run(debug=True)