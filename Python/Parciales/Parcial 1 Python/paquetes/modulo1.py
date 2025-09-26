def carga_de_partidos(parametro_lista =[]):
    print("Ingrese informacion del Jugador")
    for _ in range(3):
        edad_jugador = int(input("Ingrese edad del jugador: "))
        nombre_jugador = input("Ingrese nombre del jugador: ").lower()
        categoria = int(input("Ingrese numero de categoria del jugador 1, 2 o 3 (primera, segunda, tercera): "))
        posicion_de_juego = input("Ingrese posicion del jugador (arquero, defensor, mediocampista, delantero): ").lower()
        estadio_de_juego = input("Ingrese Estadio donde juega: ").lower() 
    
        parametro_lista.append(
            {
                "edad": edad_jugador,
                "nombre": nombre_jugador,
                "categoria": categoria,
                "posicion": posicion_de_juego,
                "estadio": estadio_de_juego
            }
        )