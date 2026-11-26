"""
Módulo de Lógica de Negocio e Interfaz de Consola
Proyecto Final - Sistema de Gestión de Productos
Captura entradas de usuario, valida tipos y restricciones, y coordina la persistencia con funciones_sql.
"""

import funciones_sql

# ==============================================================================
# FUNCIONES AUXILIARES DE VALIDACIÓN DEFENSIVA (ENTRADAS DE USUARIO)
# ==============================================================================

def pedir_texto(mensaje):
    """
    Solicita una cadena de texto por consola y garantiza que no esté vacía
    ni contenga únicamente espacios en blanco (utilizando strip()).
    """
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print("Error: El campo no puede quedar vacio. Intente nuevamente.")

def pedir_entero(mensaje, minimo=0):
    """
    Solicita un número entero y maneja excepciones ValueError para evitar caídas del sistema.
    Valida además que el número sea mayor o igual a la cota mínima especificada.
    """
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor >= minimo:
                return valor
            print(f"Error: Ingrese un valor mayor o igual a {minimo}.")
        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")

def pedir_flotante(mensaje, minimo=0.01):
    """
    Solicita un número decimal (float) con validación contra errores de conversión ValueError.
    Exige que el precio sea estrictamente positivo (mayor o igual al mínimo establecido).
    """
    while True:
        try:
            valor = float(input(mensaje).strip())
            if valor >= minimo:
                return valor
            print(f"Error: El precio debe ser mayor o igual a {minimo}.")
        except ValueError:
            print("Error: Debe ingresar un valor numerico decimal valido (use punto como separador).")

# ==============================================================================
# OPERACIONES DEL SISTEMA (CRUD + REPORTES)
# ==============================================================================

def registrar_producto():
    """
    Opción 1: Captura los datos obligatorios de un producto, valida sus tipos
    y solicita a funciones_sql la inserción parametrizada en la base de datos.
    """
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
    """
    Opción 2: Recupera y muestra todos los productos registrados en el inventario.
    Aplica formateo visual estructurado con alineación de columnas.
    """
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
    """
    Opción 3: Solicita un ID por teclado y consulta a la base de datos.
    Muestra los detalles del producto si existe o informa si no fue encontrado.
    """
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
    """
    Opción 4: Permite modificar los datos de un producto existente.
    Verifica previamente su existencia antes de solicitar los nuevos valores.
    """
    print("\n--- Actualizar Producto Existente ---")
    id_producto = pedir_entero("Ingrese el ID del producto que desea modificar: ", minimo=1)
    prod_existente = funciones_sql.buscar_producto_por_id(id_producto)

    if not prod_existente:
        print(f"\nError: No existe un producto con ID {id_producto}.")
        return

    print(f"\nModificando producto: {prod_existente[1]} (Categoria: {prod_existente[3]})")
    print("Ingrese los nuevos datos del producto:")
    nombre = pedir_texto("Nuevo nombre: ")
    descripcion = input("Nueva descripcion (opcional): ").strip()
    categoria = pedir_texto("Nueva categoria: ")
    cantidad = pedir_entero("Nueva cantidad en stock: ", minimo=0)
    precio = pedir_flotante("Nuevo precio unitario ($): ", minimo=0.01)

    exito = funciones_sql.actualizar_producto(id_producto, nombre, descripcion, categoria, cantidad, precio)
    if exito:
        print(f"\n¡Producto con ID {id_producto} actualizado correctamente!")
    else:
        print("\nError al actualizar los datos del producto.")

def eliminar_producto():
    """
    Opción 5: Solicita un ID, valida su existencia y exige confirmacion explícita (s/n)
    al usuario antes de ejecutar la baja física en la base de datos.
    """
    print("\n--- Eliminar Producto del Sistema ---")
    id_producto = pedir_entero("Ingrese el ID del producto a eliminar: ", minimo=1)
    prod = funciones_sql.buscar_producto_por_id(id_producto)

    if not prod:
        print(f"\nError: No existe ningun producto con el ID {id_producto}.")
        return

    print(f"\nProducto seleccionado: ID {prod[0]} - {prod[1]} (Stock: {prod[4]})")
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
    """
    Opción 6: Genera un reporte de alertas de productos con bajo stock.
    Filtra por cota máxima de existencias y los despliega ordenados de menor a mayor cantidad.
    """
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
