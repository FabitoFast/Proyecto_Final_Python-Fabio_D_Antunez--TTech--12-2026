import funciones_sql

def pedir_entero(mensaje, minimo=0):
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor < minimo:
                print(f"Error: El numero debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")

def registrar_producto():
    print("\n--- REGISTRO DE NUEVO PRODUCTO ---")
    
    while True:
        nombre = input("Nombre del producto: ").strip()
        if nombre:
            break
        print("Error: El nombre no puede estar vacio.")
        
    descripcion = input("Descripcion (opcional): ").strip()
    categoria = input("Categoria: ").strip()
    
    cantidad = pedir_entero("Cantidad en stock: ", minimo=0)
    precio = pedir_entero("Precio unitario: ", minimo=1)
    
    exito = funciones_sql.agregar_producto(nombre, descripcion, categoria, cantidad, precio)
    if exito:
        print("Producto registrado exitosamente en el sistema.")
    else:
        print("No se pudo registrar el producto.")

def listar_productos():
    print("\n--- CATALOGO COMPLETO DE PRODUCTOS ---")
    productos = funciones_sql.mostrar_productos()
    
    if not productos:
        print("El inventario esta vacio actualmente.")
        return
        
    print(f"{'ID':<5} | {'Nombre':<20} | {'Categoria':<15} | {'Cantidad':<10} | {'Precio':<10}")
    print("-" * 70)
    for prod in productos:
        id_prod, nombre, desc, cat, cant, precio = prod
        print(f"{id_prod:<5} | {nombre:<20} | {cat:<15} | {cant:<10} | ${precio:<9}")

def buscar_producto():
    print("\n--- BUSQUEDA DE PRODUCTO POR ID ---")
    id_producto = pedir_entero("Ingrese el ID del producto a buscar: ", minimo=1)
    
    producto = funciones_sql.buscar_producto_por_id(id_producto)
    if producto:
        id_p, nombre, desc, cat, cant, precio = producto
        print("\nInformacion del Producto:")
        print(f"  ID:          {id_p}")
        print(f"  Nombre:      {nombre}")
        print(f"  Descripcion: {desc}")
        print(f"  Categoria:   {cat}")
        print(f"  Cantidad:    {cant}")
        print(f"  Precio:      ${precio}")
    else:
        print(f"No se encontro ningun producto con el ID {id_producto}.")

def actualizar_producto():
    print("\n--- MODIFICAR PRODUCTO ---")
    id_producto = pedir_entero("Ingrese el ID del producto que desea modificar: ", minimo=1)
    
    producto = funciones_sql.buscar_producto_por_id(id_producto)
    if not producto:
        print(f"No existe un producto con el ID {id_producto}.")
        return

    print(f"Modificando producto: {producto[1]}")
    
    while True:
        nombre = input(f"Nuevo nombre [{producto[1]}]: ").strip()
        if nombre:
            break
        print("Error: El nombre no puede estar vacio.")
        
    descripcion = input(f"Nueva descripcion [{producto[2]}]: ").strip()
    categoria = input(f"Nueva categoria [{producto[3]}]: ").strip()
    
    cantidad = pedir_entero(f"Nueva cantidad [{producto[4]}]: ", minimo=0)
    precio = pedir_entero(f"Nuevo precio [{producto[5]}]: ", minimo=1)
    
    exito = funciones_sql.modificar_producto(id_producto, nombre, descripcion, categoria, cantidad, precio)
    if exito:
        print("Producto actualizado exitosamente.")
    else:
        print("Error al actualizar el producto.")

def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    id_producto = pedir_entero("Ingrese el ID del producto que desea eliminar: ", minimo=1)
    
    producto = funciones_sql.buscar_producto_por_id(id_producto)
    if not producto:
        print(f"No existe ningun producto con el ID {id_producto}.")
        return

    confirmacion = input(f"¿Esta seguro de que desea eliminar '{producto[1]}'? (s/n): ").strip().lower()
    if confirmacion == 's':
        exito = funciones_sql.eliminar_producto(id_producto)
        if exito:
            print("Producto eliminado correctamente.")
        else:
            print("Error al intentar eliminar el producto.")
    else:
        print("Operacion de eliminacion cancelada.")

def reporte_stock():
    print("\n--- REPORTE DE PRODUCTOS CON BAJO STOCK ---")
    limite = pedir_entero("Ingrese el umbral maximo de stock para el reporte: ", minimo=0)
    
    productos = funciones_sql.reporte_bajo_stock(limite)
    if not productos:
        print(f"No se encontraron productos con stock menor o igual a {limite}.")
        return
        
    print(f"{'ID':<5} | {'Nombre':<20} | {'Stock':<10} | {'Precio':<10}")
    print("-" * 55)
    for prod in productos:
        print(f"{prod[0]:<5} | {prod[1]:<20} | {prod[4]:<10} | ${prod[5]:<9}")
