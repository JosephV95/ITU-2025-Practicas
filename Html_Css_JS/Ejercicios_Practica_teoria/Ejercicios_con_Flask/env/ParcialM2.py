from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/credito", methods=['POST'])
def calcular_credito():
    datos_credito = request.get_json()
    valor_auto = int(datos_credito["valor_auto"])
    ingreso = int(datos_credito["ingreso_total"])

    if (ingreso > 30000000):
        credito = ingreso * 0.4
    else:
        credito = ingreso *0.3
    
    if (credito <= (valor_auto * 0.2) ):
        mensaje = "Crédito Aprobado."
    else:
        mensaje = "Crédito No Aprobado."

    return jsonify({
        "mensaje": mensaje,
        "credito_max": credito
    })
    
@app.route("/promedio", methods=['POST'])
def calcular_promedio():
    ingreso_total = request.get_json()
    
    promedio_final = int(ingreso_total) / 12

    return jsonify({
        "promedio": promedio_final
    })
    
if __name__ == "__main__":
    app.run(debug=True)