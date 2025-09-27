from paquetes import modulo1, modulo2

lista_jugadores = [
    {'edad': 10, 'nombre': 'Juan Pérez', 'categoria': 1, 'posicion': 'Delantero', 'estadio': 'Malvinas Argentinas'},
    {'edad': 11, 'nombre': 'Carlos Gómez', 'categoria': 2, 'posicion': 'Mediocampista', 'estadio': 'Monumental'},
    {'edad': 15, 'nombre': 'Mario lopez', 'categoria': 3, 'posicion': 'delantero', 'estadio': 'Monumental'},
    {'edad': 21, 'nombre': 'Benito Perez', 'categoria': 1, 'posicion': 'arquero', 'estadio': 'Malvinas Argentinas'},
    {'edad': 18, 'nombre': 'Armando Paredes', 'categoria': 2, 'posicion': 'defensor', 'estadio': 'Monumental'}
]

opcion = 0
while opcion != 5:
    print("\nSeleccione una opcion")
    print("1 - Cargar datos de 3 jugadores")
    print("2 - Mostrar cantidad de partidos jugados en un ESTADIO")
    print("3 - Mostrar jugadores delanteros")
    print("4 - Mostrar promedio de edad segun CATEGORIA")
    print("5 - CANCELAR")
    opcion = int(input("INGRESE SU OPCION: "))

    match opcion:
        case 1:
            modulo1.carga_de_partidos(lista_jugadores)
        case 2:
            estadio = input("Ingrese nombre del ESTADIO: ").lower()
            resultado = modulo2.fc_partidos_por_estadio( lista_jugadores, estadio)
            print(f"En el Estadio {estadio.upper()} se jugaron {resultado} partidos.")
        case 3:
            jug_delanteros = modulo2.fc_jugadores_delanteros(lista_jugadores)
            print("\nLos jugadores delanteros son: ")
            for jugador in jug_delanteros:
                print( jugador, end=", ")
        case 4:
            categoria = int(input("Ingrese numero de categoria 1, 2 o 3 (primera, segunda, tercera): "))
            res_promedio = modulo2.promedio_por_categoria(lista_jugadores, categoria)
            print(f"En la categoria {categoria} el promedio de edad es de {int(res_promedio)}")
        case 5:
            break
        case _:
            print("OPCION INVALIDA")