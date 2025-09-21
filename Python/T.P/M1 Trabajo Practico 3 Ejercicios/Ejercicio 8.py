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

import Operaciones_Ej8 as funciones_importadas 

try:
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
except ValueError:
    print("TIPO DE DATO INVALIDO: Se deben ingresar solo numeros")
else:
    res_suma = funciones_importadas.suma(numero1, numero2)
    res_resta = funciones_importadas.resta(numero1, numero2)
    res_multiplicacion = funciones_importadas.multiplicacion(numero1, numero2)
    res_division = funciones_importadas.division(numero1, numero2)

    print(f"\nLa Suma entre {numero1} y {numero2} da como resultado: {res_suma}")
    print(f"La Resta entre {numero1} y {numero2} da como resultado: {res_resta}")
    print(f"La Multiplicacion entre {numero1} y {numero2} da como resultado: {res_multiplicacion}")
    print(f"La Division entre {numero1} y {numero2} da como resultado: {res_division}")

