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

lista_nombres = ["maria", "jose", "susana", "Eli", "lucy", "sara", "luna"]
auxiliar = ""

# for i in range(5):
#     nombre = input(f"Ingese el nombre nro {i+1}: ")
#     lista_nombres.append(nombre.lower())
# print(sorted(lista_nombres))

for i in range(len(lista_nombres)):
    contador_de_iteracion = 0 #No es necesario ponerlo, solo quiero que cuente la cantidad de cambios por iteracion
    
    for j in range( i+1, len(lista_nombres)):
        # print("Comparo", lista_nombres[i] ,"con", lista_nombres[j])
        
        if lista_nombres[i].upper() > lista_nombres[j].upper(): #! El sistema lee las palabras como numeros, es decir se pueden comparar
            auxiliar = lista_nombres[i]
            lista_nombres[i] = lista_nombres[j].upper()
            lista_nombres[j] = auxiliar.upper()
            print(lista_nombres)
            contador_de_iteracion += 1
    
    print(f"En la iteracion nro {i+1} se hicieron {contador_de_iteracion} cambios")
print ("La lista final ordenada queda asi:" , lista_nombres)
        
    

"""5. Escribir un programa que permita cargar y procesar datos de alumnos del ITU en
una lista de tuplas con la siguiente forma: (nombre, dni, materia). Ejemplo:
[(“Manuel Juarez”, 19823451, “Matematica”), (“Silvana Paredes”, 22709128,
“Programacion”), (“Rosa Ortiz”, 15123978, “Redes”), (“Luciana Hernandez”,
38981374, “Programacion”)]. Hacer un menú iterativo que permita al usuario
realizar las siguientes operaciones:
 Agregar alumnos a la lista.
 Dado el DNI de un alumno, ver las materias que cursa.
 Dada una materia, mostrar la cantidad de alumnos que la cursan.
6. Cree un diccionario con los nombres de 5 personas de su familia y sus edades.
Indicar el integrante más grande y el mas chico.
7. Cree un diccionario que contenga el nombre de una ciudad, el país al que
pertenece y la cantidad de habitantes que tiene. Hacer un menú iterativo que
permita al usuario realizar las siguientes operaciones:
 Agregar ciudades
 Eliminar ciudades
 Indicar la cantidad de habitantes en un país en particular
 El porcentaje de habitantes en una ciudad de acuerdo al total registrado """