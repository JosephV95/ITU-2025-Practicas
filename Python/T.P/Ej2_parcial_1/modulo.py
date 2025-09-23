
def cargar_tareas(param_lista):
    print("Ingrese los datos")
    for i in range(3):
        legajo = int(input("Ingrese el num legajo: "))
        nombre = input("Ingrese nombre del empleado: ")
        tarea = input("Ingrese la tarea: ")
        empresa = input("Ingrese la empresa: ")
        departamento = input("Ingrese Departamento: ")
        
        param_lista.append( {"legajo": legajo, "nombre": nombre, "tarea": tarea, "empresa": empresa, "depto": departamento} )
