"""Estructuras de Datos (listas, tuplas, diccionarios)
1. Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse. 
Luego de que se termina la carga de la lista, solicitar al usuario otro número y crear una lista con los elementos de la lista original que 
sean menores que el número dado. Imprimir esta nueva lista, iterando por ella."""

# listaNumeros = []
# listaFinal = []

# numero = int(input("Ingrese un numero: "))

# while numero != 0:
#     listaNumeros.append(numero)
#     numero = int(input("Ingrese un otro numero (para terminar ingrese 0): "))
    
# numero2 = int(input("Ingrese otro numero para comparar: "))

# for num in listaNumeros:
#     if num < numero2:
#         listaFinal.append(num)

# print(f"La lista inicial de numeros es: {listaNumeros}")
# print(f"Los numeros menores a {numero2} son:")
# for i in listaFinal:
#     print(i)

"""2. Leer una secuencia de 10 números, almacenarlos en una lista y mostrar la suma de los elementos que ocupan posiciones pares y el 
mayor número de los queocupan posiciones impares. """

# listaNumeros = []
# listaPares = []
# listaImpares = []

# for _ in range(6):
#     numero = int(input("Ingrese un numero: "))
#     listaNumeros.append(numero)
 
# for i in range(0, len(listaNumeros)):
#     if i % 2 == 0:
#         listaPares.append(listaNumeros[i])
#     else:
#         listaImpares.append(listaNumeros[i])
        
# print("Los numeros con indice PAR son:", listaPares, "Y su sumatoria es de: ", sum(listaPares))
# print("Los numeros de indice IMPAR son:", listaImpares, "y el valor mas grande es:", max(listaImpares))


"""3. Dadas 2 listas A y B de igual número de elementos, se desea generar e imprimir una lista C conteniendo 
las sumas: A[i] + B[i] = C[i]. También indicar (solo imprimir por pantalla) aquellos elementos que están en A y no están en B."""

#! A la entrada no se la convirtio en int para que pueda guardar un string
# entrada = input("Ingrese un numero para la lista A (presione Z para cancelar): ") 
# lista_A = []; lista_B = []; lista_C = []

# while entrada.lower() != "z": #! Se convierte la entrada en minuscula y luego si no es un string se la convierte a numero con int()
#     lista_A.append( int(entrada) )
#     entrada = input("Ingrese otro numero para la lista A (presione Z para terminar): ")

# for num in range( len(lista_A) ):
#     numeroB = int(input("Ingrese un numero para la lista B: "))
#     lista_B.append(numeroB)
    
# for indice_A, indice_B in zip(lista_A, lista_B):
#     lista_C.append( indice_A + indice_B)
    
# print("La lista A es:",lista_A)
# print("La lista B es:",lista_B)
# print("La lista C es:",lista_C)

# for i in lista_A:
#     esta = 0
#     for j in lista_B:
#         if i == j:
#             esta = 1
#             break
#     if esta == 0:
#         print("El elemento:", i , "no esta en la lista B")

"""4. Dado una lista de 10 nombres de personas, realice un programa que cargue la
lista, la ordene de forma ascendente y la muestre por pantalla ordenado. Python
nos brinda la función “sorted” para realizar dicho procedimiento, pero la idea es
que el ejercicio se resuelva utilizando algoritmia propia de algún método de
ordenamiento existente."""

# lista_nombres = ["maria", "jose", "susana", "Eli", "lucy", "sara", "luna"]
# auxiliar = ""

# """for i in range(5):
#     nombre = input(f"Ingese el nombre nro {i+1}: ")
#     lista_nombres.append(nombre.lower()) """
# for i in range(len(lista_nombres)):
#     contador_de_iteracion = 0 #No es necesario ponerlo, solo quiero que cuente la cantidad de cambios por iteracion
    
#     for j in range( i+1, len(lista_nombres)):
#         # print("Comparo", lista_nombres[i] ,"con", lista_nombres[j])
#         if lista_nombres[i].upper() > lista_nombres[j].upper(): #! El sistema lee las palabras como numeros, es decir se pueden comparar
#             auxiliar = lista_nombres[i]
#             lista_nombres[i] = lista_nombres[j].upper()
#             lista_nombres[j] = auxiliar.upper()
#             print(lista_nombres)
#             contador_de_iteracion += 1
    
#     print(f"En la iteracion nro {i+1} se hicieron {contador_de_iteracion} cambios")
# print ("La lista final ordenada queda asi:" , lista_nombres)
        
"""5. Escribir un programa que permita cargar y procesar datos de alumnos del ITU en una lista de tuplas con la 
siguiente forma: (nombre, dni, materia). Ejemplo:[(“Manuel Juarez”, 19823451, “Matematica”), (“Silvana Paredes”, 22709128, “Programacion”), 
(“Rosa Ortiz”, 15123978, “Redes”), (“Luciana Hernandez”, 38981374, “Programacion”)]. 
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
 Agregar alumnos a la lista.
 Dado el DNI de un alumno, ver las materias que cursa.
 Dada una materia, mostrar la cantidad de alumnos que la cursan. """

# lista_materias = []
# materias_cursando = []
# cantidad_de_alumos = 0

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
#             lista_materias.append( tuple([nombre.upper(), dni, materia]))
#             print(lista_materias)
        
#         case 2:
#             dni_buscar = int(input("Ingrese el DNI a buscar: "))
#             for elemento in lista_materias:
#                 if elemento[1] == dni_buscar:
#                     materias_cursando.append( elemento[2])
#             if len(materias_cursando) > 0:
#                 print(f"El DNI {dni_buscar} cursa las materias:", materias_cursando )
#             else:
#                 print(f"El DNI {dni_buscar} no cursa materias")
                
#         case 3:
#             materia_buscar = input("Ingrese nombre de la materia: ")
#             for materia in lista_materias:
#                 if materia[2] == materia_buscar:
#                     cantidad_de_alumos += 1
#             print(f"La materia {materia_buscar} tiene {cantidad_de_alumos} alumnos.")
#         case 4:
#             break
#         case _:
#             print("OPCION INVALIDA")

"""6. Cree un diccionario con los nombres de 5 personas de su familia y sus edades.
Indicar el integrante más grande y el mas chico. """

# familia = {}
# edad_mayor = 0
# nombre_mayor = ""
# edad_menor = 300
# nombre_menor = ""

# for i in range(3):
#     nombre = input("Ingrese el nombre: ")
#     edad = int(input("Ingrese la edad: "))
    
#     familia[nombre] = edad

# for nombre, edad in familia.items():
#     if edad > edad_mayor:
#         edad_mayor = edad
#         nombre_mayor = nombre
#     if edad < edad_menor:
#         edad_menor = edad
#         nombre_menor = nombre
        
# print(f"El integrante con mayor edad es {nombre_mayor} con {edad_mayor} años de edad.")
# print(f"El integrante con menor edad es {nombre_menor} con {edad_menor} años de edad.")

"""7. Cree un diccionario que contenga el nombre de una ciudad, el país al que pertenece y la cantidad de habitantes que tiene. 
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
1 Agregar ciudades
2 Eliminar ciudades
3 Indicar la cantidad de habitantes en un país en particular
4 El porcentaje de habitantes en una ciudad de acuerdo al total registrado """

# ciudades = {
#     "mendoza": {"habitantes": 700,
#                 "pais": "argentina"},
#     "rio": {"habitantes": 500,
#                 "pais": "brazil"},
#     "cordoba": {"habitantes": 500,
#                 "pais": "argentina"},
#     "san juan": {"habitantes": 1000,
#                 "pais": "argentina"},
#     "brasilia": {"habitantes": 2000,
#                 "pais": "brazil"},
#     "jujuy": {"habitantes": 900,
#                 "pais": "argentina"},
# }
# opcion = 0

# while opcion !=5:
#     print("Ingrese una de las siguientes acciones: ")
#     print("1 - AGREGAR ciudad")
#     print("2 - ELIMINAR ciudad")
#     print("3 - VER HABITANTES por país")
#     print("4 - VER PORCENTAJE de habitantes de ciudad segun pais")
#     print("5 - Cancelar")
    
#     opcion = int(input("Ingrese su OPCION: "))
    
#     match opcion:
#         case 1:
#             ciudad = input("Ingrese nombre de CIUDAD para AGREGAR: ")
#             ciudad_info = {}
#             nro_habitantes = int(input("Ingrese NUMERO de HABITANTES: "))
#             nombre_pais = input("Ingrese el PAIS de la ciudad: ")
            
#             ciudad_info["habitantes"] = nro_habitantes
#             ciudad_info["pais"] = nombre_pais.lower()
            
#             ciudades[ciudad.lower()] = ciudad_info
                        
#         case 2:
#             ciudad_eliminar = input("Ingrese la ciudad a ELIMINAR: ").lower()
#             encontrada = 0
#             for ciudad in ciudades:
#                 if ciudad == ciudad_eliminar:
#                     encontrada = 1
#                     break
#             if encontrada == 1:
#                 ciudades.pop(ciudad_eliminar)
#                 print(ciudades , "\n")
#             else:            
#                 print(f"La ciudad {ciudad_eliminar} no esta registrada. \n")
                        
#         case 3:
#             pais = input("Ingrese nombre de PAIS para ver sus HABITANTES: ")
#             contador = 0
            
#             for ciudad, valores in ciudades.items():
#                 if valores["pais"] == pais.lower():
#                     contador += valores["habitantes"]
#                     print (f"El Pais {pais.upper()} tiene {contador} de habitantes. \n")
#                 else:
#                     print(f"El pais {pais.upper()} no esta en la lista")
            
#         case 4:
#             ciudad_ver = input("Ingrese CIUDAD para ver el PORCENTAJE DE HABITANTES: ").lower()
#             habitantes_ciudad = 0
#             pais_a_buscar = ""
#             habitantes_pais = 0
            
#             for clave, valor in ciudades.items():
#                 if clave == ciudad_ver:
#                     habitantes_ciudad = valor["habitantes"]
#                     pais_a_buscar = valor["pais"]
            
#                     for ciudad, valores in ciudades.items():
#                         if valores["pais"] == pais_a_buscar:
#                             habitantes_pais += valores["habitantes"]
                            
#                     cantidad_final = habitantes_ciudad * 100 / habitantes_pais
                    
#                     print(f"La ciudad {ciudad_ver.upper()} tiene el {cantidad_final :.2f}% de los habitantes del pais {pais_a_buscar.upper()} \n")
            
#             #! PYTHON PERMITE USAR FOR .. ELSE o WHILE... ELSE se ejecuta cuando no hubo respuesta de las iteraciones
#             else:
#                 print(f"La ciudad {ciudad_ver.upper()} no esta registrada \n")

#         case 5:
#             break
        
#         case default:
#             print("OPCION INVALIDA")