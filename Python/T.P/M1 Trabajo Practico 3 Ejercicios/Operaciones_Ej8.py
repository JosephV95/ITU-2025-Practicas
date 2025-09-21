
def suma (a, b):
    try: 
        return a + b
    except TypeError:
        print("TIPO DE DATO NO VALIDO. Se deben ingresar numeros.")

def resta (a, b):
    try:
        return a - b
    except TypeError:
        print("TIPO DE DATO NO VALIDO. Se deben ingresar numeros.")

def multiplicacion (a, b):
    try:
        return a * b
    except TypeError:
        print("TIPO DE DATO NO VALIDO. Se deben ingresar numeros.")

def division(a, b):
    try:
       return a / b
        
    except ZeroDivisionError:
        return print("NO ES POSIBLE DIVIDIR POR CERO.")
        
    except TypeError:
        print("TIPO DE DATO NO VALIDO. Se deben ingresar numeros.")
        

   