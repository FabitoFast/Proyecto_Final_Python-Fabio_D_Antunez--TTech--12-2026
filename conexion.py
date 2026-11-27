# Módulo de Conexión a la Base de Datos (SQLite3)

import sqlite3

# Nombre del archivo de base de datos local
DATABASE_NAME = "inventario.db"

def conectar():
    # Establece y retorna un objeto de conexión física con la base de datos SQLite.
    
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos '{DATABASE_NAME}': {e}")
        return None

def crear_tabla():
    # Crea la tabla 'productos' en la base de datos si aún no existe.
    
    conn = conectar()
    if conn is None:
        print("No se pudo establecer la conexión para verificar la estructura de la base de datos.")
        return

    try:
        cursor = conn.cursor()

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
        conn.close()
