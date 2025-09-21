def valida_usuario(param_usuario):
    try:
        if len(param_usuario) < 5 or len(param_usuario) > 12:
            raise ValueError ("El Usuario debe contener entre de 6 y 12 caracteres.")
        
        if not param_usuario.isalnum() :
            raise ValueError ("El Usuario solo debe tener caracteres alfanumericos")
    except ValueError as error_mensaje:
        print(error_mensaje)
        return False
    else:
        return True

def valida_clave(param_clave):
    try:
        if len(param_clave) < 8:
            raise ValueError("La contraseña debe tener un minimo de 8 caracteres.")
        
        if " " in param_clave:
            raise ValueError("La contraseña no debe contener espacios.")
        
        tiene_mayus = False
        tiene_minus = False
        tiene_numero = False
        tiene_caracter_especial = False
        
        for caracter in param_clave:
            if caracter.isupper():
                tiene_mayus = True
            elif caracter.islower():
                tiene_minus = True
            elif caracter.isdigit():
                tiene_numero = True
            else:
                tiene_caracter_especial = True
                
        if not tiene_mayus:
            raise ValueError("La contraseña DEBE TENER al menos 1 MAYUSCULA.")
        elif not tiene_minus:
            raise ValueError("La contraseña DEBE TENER al menos 1 MINUSCULA.")
        elif not tiene_numero:
            raise ValueError("La contraseña DEBE TENER al menos 1 NUMERO.")
        elif not tiene_caracter_especial:
            raise ValueError("La contraseña DEBE TENER al menos 1 CARACTER ESPECIAL.")
        
    except ValueError as mensaje_de_error:
        print( mensaje_de_error)
        # print("La Contraseña elegida no es Segura")
        return False
    else:
        return True