# Módulo de Persistencia y Acceso a Datos (SQLite3)

import sqlite3
import conexion

def registrar_producto(nombre, descripcion, categoria, cantidad, precio):
    # Inserta un nuevo producto en la tabla 'productos'
    conn = conexion.conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (nombre, descripcion, categoria, cantidad, precio))
        conn.commit()  # Confirma la transacción en la base de datos
        return True
    except sqlite3.Error as e:
        print(f"Error al registrar producto: {e}")
        conn.rollback()  # Revierte la operación si ocurre una falla
        return False
    finally:
        conn.close()

def listar_productos():
    # Recupera todos los registros del inventario ordenados por ID de forma ascendente
    conn = conexion.conectar()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT id, nombre, descripcion, categoria, cantidad, precio FROM productos ORDER BY id ASC"
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al listar productos: {e}")
        return []
    finally:
        conn.close()

def buscar_producto_por_id(id_producto):
    # Busca un producto por su clave primaria (ID)
    conn = conexion.conectar()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        query = "SELECT id, nombre, descripcion, categoria, cantidad, precio FROM productos WHERE id = ?"
        cursor.execute(query, (id_producto,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error al buscar producto: {e}")
        return None
    finally:
        conn.close()

def actualizar_nombre(id_producto, nuevo_nombre):
    # Actualiza solo el nombre del producto
    conn = conexion.conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET nombre = ? WHERE id = ?", (nuevo_nombre, id_producto))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error al actualizar nombre: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def actualizar_descripcion(id_producto, nueva_descripcion):
    # Actualiza solo la descripcion del producto
    conn = conexion.conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET descripcion = ? WHERE id = ?", (nueva_descripcion, id_producto))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error al actualizar descripcion: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def actualizar_categoria(id_producto, nueva_categoria):
    # Actualiza solo la categoria del producto
    conn = conexion.conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET categoria = ? WHERE id = ?", (nueva_categoria, id_producto))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error al actualizar categoria: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def actualizar_cantidad(id_producto, nueva_cantidad):
    # Actualiza solo el stock del producto
    conn = conexion.conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id_producto))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error al actualizar cantidad: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def actualizar_precio(id_producto, nuevo_precio):
    # Actualiza solo el precio del producto
    conn = conexion.conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (nuevo_precio, id_producto))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error al actualizar precio: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def eliminar_producto(id_producto):
    # Elimina un producto por su ID
    conn = conexion.conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error al eliminar producto: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def reporte_bajo_stock(limite):
    # Consulta productos con stock menor o igual al limite ordenados de menor a mayor
    conn = conexion.conectar()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = """
            SELECT id, nombre, descripcion, categoria, cantidad, precio
            FROM productos
            WHERE cantidad <= ?
            ORDER BY cantidad ASC, id ASC
        """
        cursor.execute(query, (limite,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error en reporte de stock: {e}")
        return []
    finally:
        conn.close()
