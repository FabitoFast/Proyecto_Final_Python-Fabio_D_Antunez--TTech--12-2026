"""
Módulo de Conexión a la Base de Datos (SQLite3)
Proyecto Final - Sistema de Gestión de Productos
Gestiona la apertura del archivo de base de datos y la inicialización de la estructura relacional.
"""

import sqlite3

# Nombre del archivo de base de datos local
DATABASE_NAME = "inventario.db"

def conectar():
    """
    Establece y retorna un objeto de conexión física con la base de datos SQLite.
    Si ocurre una excepción durante la conexión, captura el error y retorna None.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos '{DATABASE_NAME}': {e}")
        return None

def crear_tabla():
    """
    Crea la tabla 'productos' en la base de datos si aún no existe.
    Define las claves primarias autoincrementales, restricciones NOT NULL y tipos de datos relacionales:
      - id: Clave primaria autoincremental única (INTEGER).
      - nombre: Denominación del producto obligatoria (TEXT NOT NULL).
      - descripcion: Detalle opcional del artículo (TEXT).
      - categoria: Rubro o clasificación obligatoria (TEXT NOT NULL).
      - cantidad: Nivel de existencias en stock (INTEGER NOT NULL).
      - precio: Valor unitario del producto con decimales (REAL NOT NULL).
    Garantiza el cierre del canal de conexión mediante bloque finally.
    """
    conn = conectar()
    if conn is None:
        print("No se pudo establecer la conexión para verificar la estructura de la base de datos.")
        return

    try:
        cursor = conn.cursor()
        # Sentencia DDL (Data Definition Language) para crear la tabla
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                categoria TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        """)
        conn.commit()  # Confirma la creación o existencia de la estructura
    except sqlite3.Error as e:
        print(f"Error al crear o verificar la tabla 'productos': {e}")
    finally:
        conn.close()  # Libera el recurso físico de conexión
