import sqlite3
import conexion

def registrar_producto(nombre, descripcion, categoria, cantidad, precio):
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
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error al registrar producto: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def listar_productos():
    conn = conexion.conectar()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, descripcion, categoria, cantidad, precio FROM productos")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al listar productos: {e}")
        return []
    finally:
        conn.close()

def buscar_producto_por_id(id_producto):
    conn = conexion.conectar()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, descripcion, categoria, cantidad, precio FROM productos WHERE id = ?", (id_producto,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error al buscar producto: {e}")
        return None
    finally:
        conn.close()

def actualizar_producto(id_producto, nombre, descripcion, categoria, cantidad, precio):
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
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error al actualizar producto: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def eliminar_producto(id_producto):
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
