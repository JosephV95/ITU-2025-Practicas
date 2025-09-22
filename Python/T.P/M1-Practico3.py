""" 1. Escriba una función en Python que indique si un número está en un determinado rango de numeros. Ej.:
    Entrada: valor=3; lim_inferior=2; lim_superior=5
    Salida: True """
# numero = int(input("Ingrese un numero: "))
# lim_inferior = int(input("Ingrese el limite inferior: "))
# lim_superior = int(input("Ingrese el limite superior: "))

# def verificador_de_numero(parametro1, parametro2, parametro3):
#     for num in range( parametro2, parametro3+1):
#         if num == parametro1:
#             return True
       
# numero_esta_en_rango = verificador_de_numero(numero, lim_inferior, lim_superior)
# if numero_esta_en_rango:
#     print(f"\nEl numero {numero} SI esta en el rango {lim_inferior}-{lim_superior}")
# else: 
#     print(f"\nEl numero {numero} NO esta en el rango {lim_inferior}-{lim_superior}")

"""2. Escriba una función en Python que indique si un número es perfecto. Utilice una función auxiliar que calcule los 
divisores propios. Nota: Un número perfecto es un número entero positivo que es igual a la suma de sus divisores positivos.
Ej.:  Entrada: 6 (1+2+3)
      Salida: True  """
      
# def calculo_num_perfecto( param1 ):
#     suma_divisores = 0
#     for i in range( 1, param1 ):
#         if param1 % i == 0:
#             suma_divisores += i
#     if suma_divisores == param1:
#         return True
    
# numero = int(input("Ingrese un numero: "))
# if calculo_num_perfecto(numero) == True:
#     print(f"\nEl numero {numero} ES perfecto")
# else: 
#     print(f"\nEl numero {numero} NO ES perfecto")

"""3. Escriba una función en Python que reciba como parámetro una frase y 1
carácter, y devuelva si ese carácter se encuentra dentro de la frase. Además de
ello, la función debe poder indicar la cantidad de palabras que hay en la frase.  """

# frase = input("Ingrese una frase: ")
# caracter = input("Ingrese un caracter a buscar: ")

# def funcion_verificadora (param_lista, param_caracter):
#     caracter_esta = False
#     """contador_de_palabras = len(param_lista.split())"""
#     contador_de_palabras = 0
#     dentro_de_palabra = False
    
#     for i in param_lista:
#         if i == param_caracter:
#             caracter_esta = True
            
#         if i != " " and  not dentro_de_palabra:  #En Python and es (&&) y not es negacion ( !dentro_de_palabra)
#             contador_de_palabras += 1
#             dentro_de_palabra = True
#         elif i == " ": 
#             dentro_de_palabra = False
            
#     return {"esta":caracter_esta, "nro_palabras": contador_de_palabras}

# verificador = funcion_verificadora( frase, caracter)

# if verificador["esta"] :
#     print(f"\nEl caracter '{caracter}' si esta en la frase.")
#     print(f"Y la frase tiene {verificador['nro_palabras']} palabras en total")
# else:
#     print(f"\nLa palabra '{caracter}' NO esta en la frase.")
#     print(f"Y la frase tiene {verificador['nro_palabras']} palabras en total")

"""4. Escriba una función en Python que reciba una lista de valores enteros y devuelva
otra lista sólo con aquellos valores pares.
Ej.:
Entrada: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Salida: [2, 4, 6, 8]    """

# def funcion_selector_pares( param_lista ):
#     lista_de_pares = []
#     for num in param_lista:
#         if num % 2 == 0:
#             lista_de_pares.append(num)
#     return lista_de_pares

# lista_numeros = []
# opcion = 1
# while opcion != 3:
#     print("\nSeleccione su opcion: ")
#     print("1- AGREGAR numero")
#     print("2- VER numeros pares")
#     print("3- TERMINAR")
#     opcion = int(input("Ingrese su opcion: "))
    
#     match opcion:
#         case 1:
#             numero = int(input("\nIngrese un Numero: "))
#             lista_numeros.append(numero)
#         case 2:
#             num_pares = funcion_selector_pares(lista_numeros)
#             print(f"Los numeros pares son: {num_pares}")
#         case 3:
#             break
#         case default:
#             print("OPCION INVALIDA")

"""5. Escribir una función que reciba una frase y devuelva un diccionario con las
palabras que contiene y su longitud. """

# def funcion_diccionario_palabras(param_frase):
#     diccionario_palabras= {}
#     contador_caracteres = 0
#     palabra_formada = ""
    
#     for c in param_frase:
#         #? Abreviado seria  if c in " ,." Y para hacerlo al reves y que pregunte si c!= "" and c!="." and c!="," abreviado c in not " ,."
#         if c == " " or c == "," or c == ".":  
#             if len(palabra_formada) > 0:
#                 diccionario_palabras[palabra_formada] = contador_caracteres
#                 palabra_formada = ""
#                 contador_caracteres = 0
        
#         else :
#             contador_caracteres += 1
#             palabra_formada += c
        
#     #! Por si la frase no termina en espacio o punto
#     if len(palabra_formada) > 0:
#         diccionario_palabras[palabra_formada] = contador_caracteres
    
#     return diccionario_palabras

# frase = input("Ingrese su frase: ")
# diccionario_final = funcion_diccionario_palabras(frase)
# print(f"\nEl Diccionario formado es: \n{diccionario_final}")

"""6. Los empleados de una fábrica trabajan en dos turnos, Diurno y Nocturno. Se
desea calcular el jornal diario de acuerdo a las siguientes reglas:
 La tarifa de las horas diurnas es de $350
 La tarifa de las horas nocturnas es de $400
 En caso de ser festivo, la tarifa se incrementa en un 10% en caso de turno diurno y en un 15% para el nocturno.

Desarrolle una función que permita ingresar por teclado la siguiente información para, al menos, 2 empleados, nombre del trabajador,
el número de horas trabajadas, el turno y el tipo de día (“Festivo”, “Laborable”), para ello se podría utilizar 1 “diccionario” 
para registrar la información y si los datos ingresados son correctos llamar a otra función que realice el cálculo del sueldo a cobrar 
en ese día. Mostrar por pantalla los datos ingresados y el sueldo calculado para cada empleado.  """

# lista_emplados = [
#     {"nombre": "Martin", "horas_trabajadas": 5, "turno": "diurno", "dia": "festivo"},
#     {"nombre": "Sara", "horas_trabajadas": 8, "turno": "noche", "dia": "laboral"}
# ]
# def funcion_calcular_salario (param_lista_empleados):
#     for empleado in param_lista_empleados:
#         salario_calculado = 0
        
#         if empleado["turno"][0] == "d":
#             salario_calculado = 350 * empleado["horas_trabajadas"]
#         elif empleado["turno"][0] == "n": 
#             salario_calculado = 400 * empleado["horas_trabajadas"]
        
#         if empleado["dia"][0] == "l":
#             salario_calculado *= 1.1
#         elif empleado["dia"][0] == "f":
#             salario_calculado *= 1.15
            
#         empleado["salario"] = round(salario_calculado, 2) # funcion para redondear decimales
    
#     return param_lista_empleados

# opcion = 0
# while opcion != 3:
#     print("Seleccione una opcion:")
#     print("1 - Agregar Empleado.")
#     print("2 - Ver salario de empleados")
#     print("3 - Terminar")
#     opcion = int(input("INGRESE SU OPCION: "))
#     match opcion:
#         case 1:
#             nombre = input("Ingrese el nombre: ")
#             horas = int(input("Ingrese horas trabajadas: "))
#             turno = input("Ingrese turno D (diurno) o N (noche): ")
#             dia = input("Ingrese el tipo de dia, F (festivo) - L (laboral): ")
#             lista_emplados.append({
#                 "nombre": nombre, "horas_trabajadas": horas, "turno": turno, "dia": dia
#             })
#         case 2:
#             lista_final = funcion_calcular_salario(lista_emplados)
#             for empleado in lista_final:
#                 print(f"El empleado {empleado['nombre']} tiene: {empleado['horas_trabajadas']}hs. turno {empleado['turno']} en día {empleado['dia']}.\nSU SALARIO ES DE: ${empleado['salario']}\n")
#         case 3:
#             break
#         case _:
#             print("OPCION INVALIDA")

""" 7. Realice el ejercicio 5 del practico número 2 (listas de tuplas), pero
implementando la/s función/es necesaria/s.  
    Escribir un programa que permita cargar y procesar datos de alumnos del ITU en una lista de tuplas con la siguiente forma: 
    (nombre, dni, materia). Ejemplo: [(“Manuel Juarez”, 19823451, “Matematica”), (“Silvana Paredes”, 22709128, “Programacion”), 
    (“Rosa Ortiz”, 15123978, “Redes”), (“Luciana Hernandez”, 38981374, “Programacion”)]. 
    Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
         Agregar alumnos a la lista.
         Dado el DNI de un alumno, ver las materias que cursa.
         Dada una materia, mostrar la cantidad de alumnos que la cursan.    """
        
# def funcion_materias_por_dni (param_lista, param_dni):
#     materias_cursadas = []
#     for elemento in param_lista:
#         if elemento[1] == param_dni:
#             materias_cursadas.append(elemento[2])
#     return materias_cursadas
# def funcion_alumnos_por_materia( param_lista, param_materia):
#     cantidad_de_alumos = 0
#     for materia in param_lista:
#         if materia[2] == param_materia:
#             cantidad_de_alumos += 1
#     return cantidad_de_alumos
    
# lista_datos_alumnos = [('JOSE', 39, 'mate'), ('GUADA', 22, 'datos'), ('MARIANA', 25, 'mate'), ('DANTE', 21, 'fisica'), ('DANTE', 21, 'logica')]

# opcion = 0
# while opcion !=4:
#     print("Ingrese una de las siguientes opciones: ")
#     print("1 - AGREGAR alumno: ")
#     print("2 - Ver MATERIAS segun el DNI: ")
#     print("3 - Ver ALUMNOS por MATERIA: ")
#     print("4 - Cancelar")
#     opcion = int(input("Ingrese su OPCION: "))
                 
#     match opcion:
#         case 1:
#             nombre = input("Ingrese el Nombre: ")
#             dni = int(input("Ingrese el DNI: "))
#             materia = input("Ingrese la Materia: ")
#             lista_datos_alumnos.append( tuple([nombre.upper(), dni, materia.lower()]))
#             print("\n", lista_datos_alumnos)
        
#         case 2:
#             dni_buscar = int(input("Ingrese el DNI a buscar: "))
#             lista_materias_dni = funcion_materias_por_dni(param_dni= dni_buscar, param_lista= lista_datos_alumnos )
            
#             if len(lista_materias_dni) > 0:
#                 print(f"El DNI {dni_buscar} cursa las materias: {lista_materias_dni}", )
#             else:
#                 print(f"El DNI {dni_buscar} no cursa materias")
                
#         case 3:
#             materia_buscar = input("Ingrese nombre de la materia: ").lower()
#             cantidad_alumnos = funcion_alumnos_por_materia(param_materia= materia_buscar, param_lista= lista_datos_alumnos)
#             print(f"La materia {materia_buscar} tiene {cantidad_alumnos} alumnos.")
           
#         case 4:
#             break
#         case _:
#             print("OPCION INVALIDA")

"""8. Crea el siguiente módulo:
 El módulo se denominará operaciones.py y contendrá 4 funciones para realizar una suma, una resta, un producto y una division 
entre dos números. Todas ellas devolverán el resultado.
 En las funciones del módulo deberá de haber tratamiento e invocación manual
de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:
 ValueError: En caso de que se envíen valores a las funciones que no sean
números. Además deberá aparecer un mensaje que informe Error: Tipo
de dato no válido.
 ZeroDivisionError: En caso de realizar una división por cero. Además
deberá aparecer un mensaje que informe Error: No es posible dividir
entre cero.
Una vez diseñado el modulo, desarrolle un programa que, utilizando el modulo
anterior, haga uso de todas la funciones con los parámetros ingresados por
teclado """

# import Operaciones_Ej8 as funciones_importadas  #! El programa principal quedo asi, pero se le debe crear el archivo modulo (ESTA RESUELTO EN LA CARPETA M1 TP3)
# try:
#     numero1 = int(input("Ingrese el primer numero: "))
#     numero2 = int(input("Ingrese el segundo numero: "))
# except ValueError:
#     print("TIPO DE DATO INVALIDO: Se deben ingresar solo numeros")
# else:
#     res_suma = funciones_importadas.suma(numero1, numero2)
#     res_resta = funciones_importadas.resta(numero1, numero2)
#     res_multiplicacion = funciones_importadas.multiplicacion(numero1, numero2)
#     res_division = funciones_importadas.division(numero1, numero2)

#     print(f"\nLa Suma entre {numero1} y {numero2} da como resultado: {res_suma}")
#     print(f"La Resta entre {numero1} y {numero2} da como resultado: {res_resta}")
#     print(f"La Multiplicacion entre {numero1} y {numero2} da como resultado: {res_multiplicacion}")
#     print(f"La Division entre {numero1} y {numero2} da como resultado: {res_division}")

"""9. Cree un programa que pida por teclado el ingreso de un usuario y contraseña,
luego de ello utilice las funciones validaUsuario y validaClave, ambas en un
módulo llamado seguridad. Dichas funciones deben realizar lo siguiente:
validaUsuario:
 El nombre de usuario debe contener un mínimo de 6 caracteres y un
máximo de 12.
 El nombre de usuario debe ser alfanumérico. Si no lo cumple indicar el
mensaje: “El nombre de usuario puede contener solo letras y números”
 Nombre de usuario válido, retorna True
validaClave:
 La contraseña debe contener un mínimo de 8 caracteres
 Una contraseña debe contener letras minúsculas, mayúsculas, números y
al menos 1 carácter no alfanumérico
 La contraseña no puede contener espacios en blanco
 Contraseña válida, retorna True
 Contraseña no válida, retorna el mensaje: “La contraseña elegida no es
segura”  """

# EJERCICIO COMPLETADO EN CARPERTA M1 TP3


"""10. Como ejercicio, escriba una función que use la funcion tomaNumero para leer un
número del teclado y que maneje la excepción ErrorNumeroMalo.
""" 

def tomaNumero (param_num):
    try:
        if not param_num.isdigit():
            raise ValueError("Numero invalido")
    except ValueError as mensaje_error:
        print(mensaje_error)
    else:
        print("Numero correcto")
    
tomaNumero(input("Ingrese un numero: "))