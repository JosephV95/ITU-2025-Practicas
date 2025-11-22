from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, support_credentials=True)

@app.route("/lista_nombres", methods=['POST'])
def pagina_inicio():
    data_recibida = request.get_json()
    
    lista_final = sorted(data_recibida)
    print("NOMBRES ORDENADOS: ", lista_final)
    
    return jsonify({
        "nombres_ordenados": lista_final
    })

if __name__ == "__main__":
    app.run(debug=True)
