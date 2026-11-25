# Sistema de Gestión de Inventario - Trabajo Final Integrador

**Curso:** Iniciación a la Programación con Python  
**Estudiante:** Fabio D. Antúnez  
**Año:** 2026  

---

## 📌 Descripción del Proyecto
Aplicación de consola (CLI) desarrollada en Python para la administración y control de inventario de productos comerciales. El sistema implementa persistencia de datos relacional mediante SQLite3 y cuenta con una arquitectura modular por capas con validación defensiva de datos y control de excepciones.

---

## 🚀 Funcionalidades Principales (CRUD)
1. **Registrar nuevo producto:** Validación de cadenas no vacías y tipos numéricos positivos para stock y precio.
2. **Listar catálogo completo:** Visualización ordenada y tabulada en consola de todos los artículos registrados.
3. **Buscar producto por ID:** Localización exacta y muestra detallada de la ficha del producto.
4. **Actualizar datos de producto:** Modificación de registros existentes con persistencia transaccional.
5. **Eliminar producto:** Baja física del registro con confirmación obligatoria previa (`s/n`).
6. **Reporte de bajo stock:** Consulta filtrada de artículos cuya cantidad sea menor o igual a un umbral especificado.

---

## 🛠️ Arquitectura Modular
El proyecto aplica el principio de responsabilidad única dividiendo la lógica en módulos independientes:

* `conexion.py`: Gestión del canal de comunicación con SQLite (`inventario.db`) y creación de la tabla `productos` con claves primarias autonuméricas.
* `funciones_sql.py`: Capa de persistencia. Contiene las sentencias SQL parametrizadas (`?`) para neutralizar inyecciones SQL y garantizar transacciones seguras (`commit`/`rollback`).
* `funciones.py`: Capa de lógica de negocio e interfaz de consola. Gestiona las entradas del operador mediante bucles `while True` y control de excepciones `ValueError`.
* `main.py`: Punto de entrada del programa. Orquesta el menú principal interactivo y la ejecución continua del sistema.
* `.gitignore`: Configuración de exclusión para evitar el versionado de la base de datos binaria (`inventario.db`) y carpetas de caché (`__pycache__/`).

---

## 📋 Requisitos de Ejecución
* Python 3.10 o superior.
* Módulo estándar `sqlite3` (incluido nativamente en Python).

---

## 💻 Instrucciones de Puesta en Marcha

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/FabitoFast/Proyecto_Final_Python-Fabio_D_Antunez--TTech--12-2026.git
Ingresar al directorio del proyecto:
cd Proyecto_Final_Python-Fabio_D_Antunez--TTech--12-2026
Ejecutar la aplicación:
python main.py
