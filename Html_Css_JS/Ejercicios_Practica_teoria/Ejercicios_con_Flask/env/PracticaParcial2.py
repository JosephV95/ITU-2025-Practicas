from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, support_credentials=True)

@app.route("/", methods=['POST'])
def basico():
    info_recibida = request.get_json()
    
    
    return jsonify({
        "mensaje": "Hola, " + info_recibida["nombre"] + ". Bienvenido a la practica parcial 2 de Backend.",
    })
    
    
    
if __name__ == "__main__":
    app.run(debug=True) 