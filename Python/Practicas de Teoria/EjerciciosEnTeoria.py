
# ! EJERCICIOS DE LA TEORIA
""" Realizar un programa donde se pida por teclado tres números; si el primero es negativo,
debe realizar el producto de los tres y si no lo es, la suma. Mostrar los resultados. """

# num_1 = int(input("Ingrese el 1er numero: "))
# num_2 = int(input("Ingrese el 2do numero: "))
# num_3 = int(input("Ingrese el 3er numero: "))

# if num_1 < 0:
#     multiplicacion = num_1*num_2*num_3
#     print("La multiplicacion de: ", num_1, num_2, num_3, "fue de: ", multiplicacion )
# else:
#     suma = num_1+num_2+num_3
#     print("La SUMA de: ", num_1, num_2, num_3, "fue de:", suma )

""" Ejercicio para Practicar
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números comprendidos entre el cero y el número ingresado separados
por comas. Le agregamos un detalle más: mostrar la suma de todos los números.  """
# numero_1 = int(input("Ingreses un mayor a 0: "))

# while numero_1 < 0:
#     numero_1 = int(input("Ingreses un mayor a 0: "))

# for num in range(0, numero_1 + 1):
#     print(num, end=",")


""" Ejercicio para Practicar
Escribir un programa que pregunte al usuario una cantidad de dinero ($) a invertir, el
interés anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión cada año que dura la inversión. Nota: el valor inicial de cada año depende del
capital + interés obtenido en el año anterior."""

dinero= int(input("Ingrese la cantidad de dinero: "))
interes = int (input("Ingrese la cantidad de Interes: "))
anios = int(input("Ingrese la cantidad de años: "))

total= dinero

for i in range ( 1, anios + 1):
    total += (total * interes / 100)
    print( "En el año ", i, " se obtuvo en total: $", total)