def cargar_datos(param_lista):
       
    for i in range(3):
        cuit_ingreado= int(input("Ingrese el cuit: "))
        rsocial_ingresado = input("Ingrese la razon social: ")
        cod_producto_ingresado = int(input("Ingrese el codigo de producto: "))
        monto_ingresado = int(input("Ingrese el monto: "))
        
        param_lista.append( {"cuit": cuit_ingreado, "rsocial": rsocial_ingresado, "codprod": cod_producto_ingresado, "monto": monto_ingresado} )
        
        