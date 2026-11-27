# Módulo de Persistencia y Acceso a Datos (SQLite3)

import sqlite3
import conexion

def registrar_producto(nombre, descripcion, categoria, cantidad, precio):
    # Inserta un nuevo producto en la tabla 'productos'.
    
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
    # Recupera todos los registros del inventario ordenados por ID de forma ascendente.Retorna una lista de tuplas con los productos encontrados.

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
    # Busca un producto específico a partir de su clave primaria (ID).

    conn = conexion.conectar()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        query = "SELECT id, nombre, descripcion, categoria, cantidad, precio FROM productos WHERE id = ?"
    # El parámetro se pasa como tupla de un solo elemento (id_producto,)
        cursor.execute(query, (id_producto,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error al buscar producto: {e}")
        return None
    finally:
        conn.close()

def actualizar_producto(id_producto, nombre, descripcion, categoria, cantidad, precio):
    # Modifica los atributos de un producto existente identificado por su ID.
    
    conn = conexion.conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        query = """
            UPDATE productos
            SET nombre = ?, descripcion = ?, categoria = ?, cantidad = ?, precio = ?
            WHERE id = ?
        """
        cursor.execute(query, (nombre, descripcion, categoria, cantidad, precio, id_producto))
        conn.commit()
        # cursor.rowcount verifica cuántas filas fueron afectadas
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error al actualizar producto: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def eliminar_producto(id_producto):
    # Elimina físicamente un producto de la base de datos según su ID.
    
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
    # Consulta productos con existencias menores o iguales a un umbral dado.
    
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
