from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, support_credentials=True)

@app.route("/globulos", methods= ['POST'])
def verificar_globulos():
    datosRecibidos = request.get_json()
    
    if int(datosRecibidos["rojos"]) > 40  or  int(datosRecibidos["blancos"]) > 40:
        return jsonify({
            "mensaje": "Precaución: Valores de glóbulos elevados. Lo normal es hasta 40.",
        })
    else:
        return jsonify({
            "mensaje": "Sus valores de glóbulos están dentro de los parámetros normales.",
        })
         
         
@app.route("/trigliceridos", methods= ['POST'])
def verifcar_trigliceridos():
    datosRecibidos = request.get_json()
    
    if int(datosRecibidos) > 70:
        return jsonify({
            "mensaje": "Precaución: Valores de triglicéridos elevados. Lo normal es hasta 70.",
        })
    else:
        return jsonify({
            "mensaje": "Sus valores de triglicéridos son normales.",
        })
        
if __name__ == "__main__":
    app.run(debug = True)