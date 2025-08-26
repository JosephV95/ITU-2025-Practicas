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

# lista_de_nros = []
# total = 0

# while total <= 50 and len(lista_de_nros) < 10:
#      numero = int(input("Ingrese un numero a sumar:"))
#      lista_de_nros.append(numero)
#      total += numero
# print("Los numeros a sumar fueron:", lista_de_nros, "y la suma total fue de:", total)

"""5. Cálculo de los salarios mensuales de los empleados de una empresa, sabiendo que éstos se calculan en base a las horas semanales 
trabajadas y de acuerdo a un precio especificado por horas. Si se pasan de cuarenta horas semanales, las horas
extraordinarias se pagarán a razón de 1,5 veces la hora ordinaria."""

# horas_trabajadas = int(input("Ingresa las horas semanales trabajadas: "))
# precio_hora = int(input("Ingrese el precio de la hora de trabajo: "))

# if horas_trabajadas > 40:
#      salario = 40 * precio_hora + (horas_trabajadas - 40) * (precio_hora * 1.5)
#      print("El Salario por", horas_trabajadas, "hs. de trabajo es de: $", salario )
# else:
#      salario= horas_trabajadas * precio_hora
#      print("El salario por", horas_trabajadas, "hs. de trabajo es de: $", salario)

"""6. Escribir un programa que pregunte al usuario una cantidad de dinero ($) a invertir, el interés anual y el número de años, y 
muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión. Nota: el valor inicial de
cada año depende del capital + interés obtenido en el año anterior."""

# dinero = int(input("Ingrese la cantidad de dinero a invertir: "))
# interes = int(input("Ingrese la tasa de interes: "))
# anios = int (input("Ingrese la cantidad de años: "))

# dinero_total = dinero

# for num in range(1, anios + 1):
#      dinero_total = dinero_total + dinero_total * interes / 100
#      print("El dinero total para el anio", num, "fue de: $", round(dinero_total, 2)) #! round() sirve para limitar la cantidad de decimales, con el segundo valor (,2)

"""7. Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: si el promedio global obtenido 
por un alumno en el último periodo es mayor o igual que 4, se le hará un descuento del 30% sobre la matrícula y no se le cobrará IVA; 
si el promedio obtenido es menor que 4 deberá pagar la matrícula completa, la cual debe incluir el 10% de IVA. Hacer un algoritmo que
calcule el valor a pagar si se conocen las notas finales de las 6 materias que cursaron."""

costo_matricula = int(input("Ingrese el Costa de la Matricula: "))
lista_notas = []
suma_notas = 0
 
for i in range(1, 7):
     # nota = int(input("Ingrese la nota", i ,": ")) #!input solo espera recibir 1 solo valor, con las comas se le esta pidiendo que sean 3, por eso da error
     nota = int(input( f"Ingrese la nota {i}:")) #? esto es un f-string (cadena formateada) que permite meter variables dentro del texto.
     while nota > 10:
          nota = int(input( f"Ingrese la nota {i} (debe ser menor a 10):"))
     
     lista_notas.append(nota)

for num_nota in lista_notas:
     suma_notas += num_nota

if suma_notas / len(lista_notas) >= 4 :
     matricula_final = costo_matricula * 0.7
     print("Felicidades se desconto 30% en el costo de la matricula, deberas abonar: $", round(matricula_final, 2))
else:
     matricula_final= costo_matricula * 1.1
     print("No alcanzaste los requisitos para el descuento, deberas abonar: $", round(matricula_final, 2))