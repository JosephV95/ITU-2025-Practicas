from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = "CLAVE_PARA QUE FUNCIONE SESSION"

@app.route("/")
def inicio():
    return render_template("Ejercicio_10_login.html")

@app.route('/login', methods=['POST'])
def login():
    diccionario_usuarios = {"sara": "123", "lara": "123", "maria": "123", "ana": "123"}
    dataRecibida = request.get_json()
    
    # Aca guardo si se encontro el usuario y tambien voy empezando el mensaje a devolver
    usuario_encontrado = 0
    mensaje_a_devolver = "TODO OK"
    
    for usuario in diccionario_usuarios:
        if usuario == dataRecibida["usuario"].lower():
            usuario_encontrado = 1
            if diccionario_usuarios[usuario] != dataRecibida["contraseña"].lower():
                mensaje_a_devolver = "La contraseña es incorrecta"
    
    if usuario_encontrado == 0:
        mensaje_a_devolver = "El usuario ingresado no existe"
    
    # Aca voy a guardar que el usuario esta logueado ( en session )
    if mensaje_a_devolver == "TODO OK":
        session['UsuarioLogueado'] = True
  
    return jsonify({"mensaje": mensaje_a_devolver})             
  
# Ruta que verifica si el usuario esta logueado o no segun lo guardado en session
@app.route("/validar_session")
def validar_session():
    try:
        if session['UsuarioLogueado'] == True:
            return render_template("Ejercicio_10_operacion.html")
    except KeyError:
        return "NO ESTA LOGUEADO"
    
  
@app.route("/operacion", methods=['POST'])
def operacion():
    
    try:
        if session['UsuarioLogueado'] == True:
            dataRecibida = request.get_json()
            operacion = dataRecibida['operacion']
            cantidad = int( dataRecibida['cantidad'] )
            
            # session["saldo_total"] = 0  # No me conviene iniciarlo en 0 porque cada vez que se llame a esta funcion se resetearia el saldo
            mensaje_a_devolver = ""
            
            if operacion == "depositar":
                session["saldo_total"] += cantidad
                mensaje_a_devolver = f"Deposito ${cantidad}. Su Saldo es de: ${session['saldo_total']}"
                
            elif operacion == "retirar":
                session["saldo_total"] -= cantidad
                mensaje_a_devolver = f"Retiro ${cantidad}. Su Saldo es de: ${session['saldo_total']}"
            elif operacion == "transferir":
                session["saldo_total"] -= cantidad
                mensaje_a_devolver = f"Transfirio ${cantidad}. Su Saldo es de: ${session['saldo_total']}"
            elif operacion == "saldo":
                mensaje_a_devolver = f"Su Saldo es de: ${session['saldo_total']}"
            
            return jsonify({"mensaje": mensaje_a_devolver})
            
    except KeyError:
        return jsonify({"mensaje_operacion": "NO ESTA LOGUEADO"})
    
    
if __name__ == '__main__':
    app.run( debug = True )
    