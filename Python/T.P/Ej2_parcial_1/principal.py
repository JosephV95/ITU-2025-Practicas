import modulo

def emplados_en_empresa(param_lista, empresa):
    sumatoria = 0
    for empleado in param_lista:
        if empleado["empresa"] == empresa:
            sumatoria += 1
    return sumatoria

def nombres_tarea (param_lista, tarea):
    lista_empleados = []
    
    for elemento in param_lista:
        if elemento["tarea"] == tarea:
            lista_empleados.append( elemento["nombre"])
    return lista_empleados

def empleados_por_departamento(param_lista, departamento):
    dicc_empresas = {}
    
    for elemento in param_lista:
        if elemento["depto"] == departamento:
            nombre_empresa = elemento["empresa"]
            if nombre_empresa in dicc_empresas:
                dicc_empresas[nombre_empresa] += 1
            else:
                dicc_empresas[nombre_empresa] = 1
            
    return dicc_empresas

lista_tareas = [
    {"legajo": 12, "nombre": "mari", "tarea": "gerente", "empresa": "sprite", "depto": "marketing"},
    {"legajo": 11, "nombre": "Rei", "tarea": "oficina", "empresa": "coca cola", "depto": "marketing"},
    {"legajo": 10, "nombre": "jonny", "tarea": "limpieza", "empresa": "coca cola", "depto": "marketing"},
    {"legajo": 15, "nombre": "juan", "tarea": "oficina", "empresa": "pepsi", "depto": "ventas"}
]

opcion = 0
while opcion != 5:
    print("\nSELECCIONE UNA OPCION")
    print("1- Cargar 3 tareas")
    print("2- Mostrar cantidad de empleados en una Empresa")
    print("3- Mostrar nombres de empleados por TAREA")
    print("4- Mostrar cantidad de empleados en empresas segun DEPARTAMENTO")
    print("5- CANCELAR")
    opcion = int(input("INGRESE SU OPCION: "))
    
    match opcion:
        case 1:
            modulo.cargar_tareas(lista_tareas)
        case 2:
            empresa = input("Ingrese nombre de la empresa: ")
            cantidad = emplados_en_empresa(lista_tareas, empresa)
            print(f"En la empresa {empresa} hay {cantidad} de empleados")
        case 3:
            tarea = input("Ingrese nombre de la tarea: ")
            lista_nombres = nombres_tarea(lista_tareas, tarea)
            print(f"Los nombres que hacen la tarea {tarea} son: {lista_nombres}")
        case 4:
            depa = input ("Ingrese el departamento: ")
            resultado = empleados_por_departamento(lista_tareas, depa)
            for clave, valor in resultado.items():
                print(f"La empresa {clave} tiene {valor} empleados en el departamento {depa}")
        
        case 5:
            break
        case _:
            print("OPCION INVALIDA")