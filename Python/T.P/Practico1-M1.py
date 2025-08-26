""" Practico Modulo 1 - Python
#? Algoritmia – Control de Flujo
1. Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla 
la cadena ¡Hola<nombre>!, donde <nombre> es el nombre que el usuario haya introducido.""" 

# nombre = input("Escriba su nombre: ")
# print("¡Hola ", nombre, "!")

"""2. Realiza el programa necesario para determinar cuáles son los múltiplos de 5 comprendidos entre 1 y N, donde N se ingresa por 
teclado (controlar que N contenga un valor positivo mayor o igual a 5). """

# numero = int(input("Ingrese un Numero mayor o igual a 5: "))

# while numero < 5:
#     numero = int(input("Ingrese un Numero mayor o igual a 5: "))
    
# for num in range(1, numero + 1):
#     if num % 5 == 0:
#         print(num, end=', ')

"""3. Leer una secuencia de números y determinar el mayor de los pares leídos.
PD: podría ingresar números hasta que el usuario ingrese un negativo o cero."""
# numero = int(input("Ingrese un Numero: "))
# lista = []
# lista.append(numero)
# par_mayor = 0

# while numero > 0:
#     numero = int(input("Ingrese otro Numero: "))
#     lista.append(numero)
    
# for num in lista:
#     if num % 2 == 0 and num > par_mayor:
#         par_mayor = num
    
# print("En la lista ", lista, "el número par mayor es:", par_mayor)

"""4. Elabore un programa que sume números ingresados por el usuario y que su ejecución finalice cuando la suma de los números 
sea mayor a 50 o bien cuando la cantidad de números ingresados sea mayor a 10. Cuando se cumple alguna de
las condiciones de finalización, se debe mostrar la suma de todos los números."""

"""5. Cálculo de los salarios mensuales de los empleados de una empresa, sabiendo que éstos se calculan en base a las horas semanales 
trabajadas y de acuerdo a un precio especificado por horas. Si se pasan de cuarenta horas semanales, las horas
extraordinarias se pagarán a razón de 1,5 veces la hora ordinaria."""

"""6. Escribir un programa que pregunte al usuario una cantidad de dinero ($) a invertir, el interés anual y el número de años, y 
muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión. Nota: el valor inicial de
cada año depende del capital + interés obtenido en el año anterior."""

"""7. Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: si el promedio global obtenido 
por un alumno en el último periodo es mayor o igual que 4, se le hará un descuento del 30% sobre la matrícula y no se le cobrará IVA; 
si el promedio obtenido es menor que 4 deberá pagar la matrícula completa, la cual debe incluir el 10% de IVA. Hacer un algoritmo que
calcule el valor a pagar si se conocen las notas finales de las 6 materias que cursaron."""
