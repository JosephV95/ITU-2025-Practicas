from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)

CORS(app, support_credentials=True)

@app.route("/promedio", methods=['GET', 'POST'])
def calcular_promedio():
    datos_notas = request.get_json()
    suma_promedio = 0
    nota_alta = 0
    
    for valor_nota in datos_notas.values():
        suma_promedio += int(valor_nota)
        if int(valor_nota) > nota_alta:
            nota_alta = int(valor_nota)
            
    promedio = suma_promedio / len(datos_notas)
    return jsonify({
        "promedio": promedio,
        "nota_mas_alta": nota_alta
    } )
    
@app.route("/verificar_edad", methods=['POST'])
def verificar_edad():
    dato_edad = request.get_json()
    
    fecha_nacimiento = datetime.strptime(dato_edad, "%Y-%m-%d").date()
    fecha_actual = datetime.now().date()
    
    # Calcular edad - tambien comprueba el mes y el dia para verificar si ya cumplio años este año
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

    print("EDAD: ", edad)
    if edad >= 18:
        return jsonify({"mayor": True, "mensaje": "SI es mayor de edad.", "edad": edad})
    else:
        return jsonify({"mayor": False, "mensaje": "NO es mayor de edad.", "edad": edad})


if __name__ == "__main__":
    app.run(debug=True)