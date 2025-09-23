import funciones_importar

def promedio(param_lista):
    sumatoria = 0
    for venta in param_lista:
        sumatoria += venta["monto"]
    
    return sumatoria / len(param_lista)

def ventas_por_cuit (param_lista, cuit_elegido):
    ventas_del_cuit = []
    for venta in param_lista:
        if venta["cuit"] == cuit_elegido:
            ventas_del_cuit.append( venta )
            
    return ventas_del_cuit

def compra_mas_alta(param_lista):
    compra_mas_alta = 0
    nombre_cliente = ""
    
    for venta in param_lista:
        if venta["monto"] > compra_mas_alta:
            compra_mas_alta = venta["monto"]
            nombre_cliente = venta["rsocial"]
    # return { "nombre": nombre_cliente, "monto": compra_mas_alta }
    return [nombre_cliente, compra_mas_alta]
    
lista_ventas_hoy = [
    {'cuit': 23, 'rsocial': 'luis', 'codprod': 1995, 'monto': 2500}, {'cuit': 12, 'rsocial': 'mar', 'codprod': 2001, 'monto': 3000}, 
    {'cuit': 13, 'rsocial': 'sdf', 'codprod': 23, 'monto': 33}, {'cuit': 12, 'rsocial': 'Lucia', 'codprod': 57, 'monto': 10111}
]

opcion = 0
while opcion !=5:
    print("\nSeleccione una opcion")
    print("1 - Cargar datos de 3 ventas")
    print("2 - Ver promedio de ventas del dia")
    print("3 - Ver ventas realizadas por un CUIT")
    print("4 - Ver cliente que realizo la compra mas alta")
    print("5 - TERMINAR")
    opcion = int(input("Ingrese su opcion: "))
    
    match opcion:
        case 1:
            funciones_importar.cargar_datos(lista_ventas_hoy)
        case 2:
            res_promedio = promedio(lista_ventas_hoy)
            print(f"El promedio de ventas fue de ${res_promedio:.2f}")
        case 3:
            cuit = int(input("Ingrese el cuit: "))
            ventas_cuit = ventas_por_cuit(lista_ventas_hoy, cuit)
            print(f"El cuit {cuit} vendio: {ventas_cuit} \n")
        case 4:
            cliente = compra_mas_alta(lista_ventas_hoy)
            # print(f"la venta mas alta fue de: {cliente['nombre']} por ${cliente['monto']}" )
            print(f"El cliente que hizo la compra más alta fue: {cliente[0]} por ${cliente[1]}" )
        case 5:
            break
        case _:
            print("OPCION INVALIDA")
            
            