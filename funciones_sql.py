import sqlite3
import conexion

def agregar_producto(nombre, descripcion, categoria, cantidad, precio):
    try:
        con = conexion.conectar()
        cursor = con.cursor()
        query = """
            INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (nombre, descripcion, categoria, cantidad, precio))
        con.commit()
        return True
    except sqlite3.Error as error:
        print(f"Error al agregar producto: {error}")
        return False
    finally:
        con.close()

def mostrar_productos():
    try:
        con = conexion.conectar()
        cursor = con.cursor()
        query = "SELECT id, nombre, descripcion, categoria, cantidad, precio FROM productos"
        cursor.execute(query)
        productos = cursor.fetchall()
        return productos
    except sqlite3.Error as error:
        print(f"Error al consultar productos: {error}")
        return []
    finally:
        con.close()

def buscar_producto_por_id(id_producto):
    try:
        con = conexion.conectar()
        cursor = con.cursor()
        query = "SELECT id, nombre, descripcion, categoria, cantidad, precio FROM productos WHERE id = ?"
        cursor.execute(query, (id_producto,))
        producto = cursor.fetchone()
        return producto
    except sqlite3.Error as error:
        print(f"Error al buscar producto: {error}")
        return None
    finally:
        con.close()

def modificar_producto(id_producto, nombre, descripcion, categoria, cantidad, precio):
    try:
        con = conexion.conectar()
        cursor = con.cursor()
        query = """
            UPDATE productos
            SET nombre = ?, descripcion = ?, categoria = ?, cantidad = ?, precio = ?
            WHERE id = ?
        """
        cursor.execute(query, (nombre, descripcion, categoria, cantidad, precio, id_producto))
        con.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as error:
        print(f"Error al modificar producto: {error}")
        return False
    finally:
        con.close()

def eliminar_producto(id_producto):
    try:
        con = conexion.conectar()
        cursor = con.cursor()
        query = "DELETE FROM productos WHERE id = ?"
        cursor.execute(query, (id_producto,))
        con.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as error:
        print(f"Error al eliminar producto: {error}")
        return False
    finally:
        con.close()

def reporte_bajo_stock(limite):
    try:
        con = conexion.conectar()
        cursor = con.cursor()
        query = "SELECT id, nombre, descripcion, categoria, cantidad, precio FROM productos WHERE cantidad <= ?"
        cursor.execute(query, (limite,))
        productos = cursor.fetchall()
        return productos
    except sqlite3.Error as error:
        print(f"Error en reporte de stock: {error}")
        return []
    finally:
        con.close()
