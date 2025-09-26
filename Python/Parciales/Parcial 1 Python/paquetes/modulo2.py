def fc_partidos_por_estadio(param_lista, param_estadio):
    total_partidos = 0

    for elemento in param_lista:
        if elemento["estadio"] == param_estadio:
            total_partidos += 1

    return total_partidos

def fc_jugadores_delanteros(param_lista):
    lista_nueva = []
    for elemento in param_lista:
        if elemento["posicion"].lower() == "delantero" :
            lista_nueva.append(elemento["nombre"])
    return lista_nueva

def promedio_por_categoria(param_lista, num_categoria):
    suma_edades= 0
    cantidad_jugadores = 0

    for elemento in param_lista:
        if elemento["categoria"] == num_categoria:
            suma_edades += elemento["edad"]
            cantidad_jugadores += 1
    
    return suma_edades / cantidad_jugadores