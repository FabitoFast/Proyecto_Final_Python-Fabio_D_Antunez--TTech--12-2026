# Módulo de Lógica de Negocio e Interfaz de Consola

import funciones_sql

# Validaciones de entrada

def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print("Error: El campo no puede quedar vacio. Intente nuevamente.")

def pedir_entero(mensaje, minimo=0):
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor >= minimo:
                return valor
            print(f"Error: Ingrese un valor mayor o igual a {minimo}.")
        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")

def pedir_flotante(mensaje, minimo=0.01):
    while True:
        try:
            valor = float(input(mensaje).strip())
            if valor >= minimo:
                return valor
            print(f"Error: El precio debe ser mayor o igual a {minimo}.")
        except ValueError:
            print("Error: Debe ingresar un valor numerico decimal valido (use punto como separador).")

# OPERACIONES DEL SISTEMA (CRUD + REPORTES)

def registrar_producto():
    print("\n--- Registrar Nuevo Producto ---")
    nombre = pedir_texto("Ingrese nombre del producto: ")
    descripcion = input("Ingrese descripcion (opcional): ").strip()
    categoria = pedir_texto("Ingrese categoria: ")
    cantidad = pedir_entero("Ingrese cantidad en stock: ", minimo=0)
    precio = pedir_flotante("Ingrese precio unitario ($): ", minimo=0.01)

    exito = funciones_sql.registrar_producto(nombre, descripcion, categoria, cantidad, precio)
    if exito:
        print("\n¡Producto registrado exitosamente en la base de datos!")
    else:
        print("\nError al registrar el producto en el sistema.")

def listar_productos():
    print("\n--- Catalogo General de Productos ---")
    productos = funciones_sql.listar_productos()

    if not productos:
        print("No hay productos registrados en el inventario.")
        return

    # Encabezado formateado
    print(f"{'ID':<5} | {'Nombre':<20} | {'Categoria':<15} | {'Stock':<8} | {'Precio ($)':<10} | {'Descripcion'}")
    print("-" * 80)
    for prod in productos:
        p_id, p_nom, p_desc, p_cat, p_cant, p_prec = prod
        desc_corta = (p_desc[:17] + '...') if len(p_desc) > 20 else p_desc
        print(f"{p_id:<5} | {p_nom:<20} | {p_cat:<15} | {p_cant:<8} | {p_prec:<10.2f} | {desc_corta}")
    print("-" * 80)

def buscar_producto():
    print("\n--- Busqueda de Producto por ID ---")
    id_producto = pedir_entero("Ingrese el ID del producto a buscar: ", minimo=1)
    prod = funciones_sql.buscar_producto_por_id(id_producto)

    if prod:
        p_id, p_nom, p_desc, p_cat, p_cant, p_prec = prod
        print("\nInformacion del Producto:")
        print(f"  ID         : {p_id}")
        print(f"  Nombre     : {p_nom}")
        print(f"  Descripcion: {p_desc if p_desc else '(Sin descripcion)'}")
        print(f"  Categoria  : {p_cat}")
        print(f"  Cantidad   : {p_cant} unidades")
        print(f"  Precio     : $ {p_prec:.2f}")
    else:
        print(f"\nNo se encontro ningun producto registrado con el ID {id_producto}.")

def actualizar_producto():
    print("\n--- Actualizar Producto Existente ---")
    id_producto = pedir_entero("Ingrese el ID del producto que desea modificar: ", minimo=1)
    prod = funciones_sql.buscar_producto_por_id(id_producto)

    if not prod:
        print(f"\nError: No existe un producto registrado con el ID {id_producto}.")
        return

    p_id, p_nom, p_desc, p_cat, p_cant, p_prec = prod
    print(f"\nProducto actual: [{p_id}] {p_nom} | Categoria: {p_cat} | Stock: {p_cant} | Precio: ${p_prec:.2f}")
    print("\nCampos para actualizar:")
    print("1. Actualizar nombre")
    print("2. Actualizar descripcion")
    print("3. Actualizar categoria")
    print("4. Actualizar cantidad")
    print("5. Actualizar precio")

    opcion = input("Seleccione la opcion deseada: ").strip()

    match opcion:
        case "1":
            nuevo_nombre = pedir_texto("Ingrese el nuevo nombre del producto: ")
            if funciones_sql.actualizar_nombre(id_producto, nuevo_nombre):
                print("El nombre del producto ha sido actualizado")
            else:
                print("Error al actualizar el nombre")
        case "2":
            nueva_desc = input("Ingrese la nueva descripcion del producto: ").strip()
            if funciones_sql.actualizar_descripcion(id_producto, nueva_desc):
                print("La descripcion del producto ha sido actualizada")
            else:
                print("Error al actualizar la descripcion")
        case "3":
            nueva_cat = pedir_texto("Ingrese la nueva categoria del producto: ")
            if funciones_sql.actualizar_categoria(id_producto, nueva_cat):
                print("La categoria del producto ha sido actualizada")
            else:
                print("Error al actualizar la categoria")
        case "4":
            nueva_cant = pedir_entero("Ingrese el nuevo stock del producto: ", minimo=0)
            if funciones_sql.actualizar_cantidad(id_producto, nueva_cant):
                print("La cantidad del producto ha sido actualizada")
            else:
                print("Error al actualizar la cantidad")
        case "5":
            nuevo_precio = pedir_flotante("Ingrese el nuevo precio del producto: ", minimo=0.01)
            if funciones_sql.actualizar_precio(id_producto, nuevo_precio):
                print("El precio del producto ha sido actualizado")
            else:
                print("Error al actualizar el precio")
        case _:
            print("La opcion ingresada no es valida")

def eliminar_producto():
    print("\n--- Eliminar Producto del Sistema ---")
    id_producto = pedir_entero("Ingrese el ID del producto a eliminar: ", minimo=1)
    prod = funciones_sql.buscar_producto_por_id(id_producto)

    if not prod:
        print(f"\nError: No existe ningun producto con el ID {id_producto}.")
        return

    p_id, p_nom, _, _, p_cant, _ = prod
    print(f"\nProducto seleccionado: ID {p_id} - {p_nom} (Stock actual: {p_cant})")
    confirmacion = input("¿Esta seguro de que desea eliminar este producto? (s/n): ").strip().lower()

    if confirmacion == 's':
        exito = funciones_sql.eliminar_producto(id_producto)
        if exito:
            print(f"\n¡Producto con ID {id_producto} eliminado con exito!")
        else:
            print("\nError al intentar eliminar el producto.")
    else:
        print("\nOperacion de eliminacion cancelada por el usuario.")

def reporte_stock():
    print("\n--- Reporte de Stock Minimo ---")
    limite = pedir_entero("Ingrese el umbral de cantidad para la alerta: ", minimo=0)
    productos = funciones_sql.reporte_bajo_stock(limite)

    if not productos:
        print(f"\nNo se encontraron productos con stock igual o inferior a {limite} unidades.")
        return

    print(f"\nAlertas encontradas (Stock <= {limite}):")
    print(f"{'ID':<5} | {'Nombre':<20} | {'Stock':<8} | {'Precio ($)':<10} | {'Categoria'}")
    print("-" * 65)
    for prod in productos:
        p_id, p_nom, _, p_cat, p_cant, p_prec = prod
        print(f"{p_id:<5} | {p_nom:<20} | {p_cant:<8} | {p_prec:<10.2f} | {p_cat}")
    print("-" * 65)
