def buscar_producto_por_id(listaProductos, idBusqueda):
    '''
        Esta funcion va a retornar el primer producto cuyo id coincida
        con el id de busqueda del usuario
    '''
    #1. Progrmar una iteracion o recorrer la lista de productos
    for productoSeleccionado in listaProductos:
        #2. Comparar el id de busqueda con el id del producto seleccionado
        if productoSeleccionado.get("id") == idBusqueda:
            return productoSeleccionado
    return None


def eliminar_producto_por_id(listaProductos, idObjetivo):
    '''
        Esta funcion debe retornar true si el producto se encuentra
        y se elimina y false si el producto no esta en la lista
    '''
    for productoSeleccionado in listaProductos:
        if productoSeleccionado["id"]==idObjetivo:
            listaProductos.remove(productoSeleccionado)
            return True
        #else: Solucion utilizando boolean para devolver el mensaje 1 sola vez si no esta el id a eliminar
            #print(f"No se encontro el producto a eliminar con id {idObjetivo}")
    return False