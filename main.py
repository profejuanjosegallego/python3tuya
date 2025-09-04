from funciones import buscar_producto_por_id, eliminar_producto_por_id


#Gestion el inventario de una tienda online administrada por el grupo TUYA
#productos-->id, nombre, descripcion, fotografia, precioUnitario, cantidadBodega
#Generar a tarves cli --> menu DE OPCIONES (REPITA INFINITAMENTE HASTA QUE EL USUARIO LO DETERMINE)
#Menu:
#1-->Registrar un producto en la app
#2-->Mostrar de forma ordenada e individual cada producto de la app
#3-->Calcular el costo total de la bodega almacenada 
#4-->Mostrar un producto en especifico (Buscar por id)
#5-->Eliminar de la bodega todos los productos asociados a un ID especifico
#0-->SALIR termine el programa

#Uso de variables ye structuras de datos 

#1REPETIR UNAS SALIDAS EN PANTALLA

opcionDelMenu=150
productos=[] #Lista

print("****Aplicacion TUYA.COM******")
print("****************************")
while opcionDelMenu != 0:
    print("1. Registar un Producto en la APP")
    print("2. Mostrar productos en bodega")
    print("3. Valorar bodega")
    print("4. Buscar un producto")
    print("5. Eliminar un producto")
    print("Digita 0 para SALIR DE LA APP")
    opcionDelMenu=int(input("Digita una opcion: "))
    #ZONA DE COMPARACIONES
    #Debo comparar lo que el usuario digita con las opciones habilitadas
    if opcionDelMenu == 0:
        print("Saliendo de la app...")
        break
    elif opcionDelMenu ==1:
        #Debo crear un diccionario desde cero para almacenar la ifnormacion de 1 producto
        producto={} #Diccionario
        
        print("Ingresando un producto a nuestra app: ")
        producto["id"]=int(input("Digita el id del producto a registar: "))
        producto["nombre"]=input("Digita el nombre del producto a registar: ")
        producto["descripcion"]=input("Cuentanos algo del producro que quieras resaltar: ")
        producto["fotografia"]=input("Ingresa la URL de la fotografia del producto: ")
        producto["precioUnitario"]=float(input("Digita el precio unitario del producto: "))
        producto["cantidadBodega"]=int(input("Digita la cantidad del producto en bodega: "))
        
        productos.append(producto) #Lista que se carga con diccionarios
        print("Producto agregado con exito \n")

    elif opcionDelMenu ==2: #SI NO HAY NADA MENSAJE DE QUE NO HAY NADA
        
        print("Mostrando los productos en bodega: ")
        for productoSeleccionado in productos:
            #producto: TV ----- precioUnitario: $500 ------ cantidad en bodega: 50
            print(productoSeleccionado)


    elif opcionDelMenu ==3:
        pass
    elif opcionDelMenu ==4:
        print("Buscando un producto por ID")
        idABuscar=int(input("Digita el id del producto que quieres buscar:  "))
        productoEncontrado=buscar_producto_por_id(productos,idABuscar)
        print(productoEncontrado)
        #Si el producto encontrado es None devolver un mensaje de que el producto no es encontrado

    elif opcionDelMenu ==5:
        print("Eliminando un producto")
        idABuscar=int(input("Digita el id del producto que quieres buscar:  "))
        if eliminar_producto_por_id(productos,idABuscar):
            print("Eliminamos con exito")
        else:
            print("opps hemos tenido problemas para eliminar el usuario indicado") 
    else:
        pass