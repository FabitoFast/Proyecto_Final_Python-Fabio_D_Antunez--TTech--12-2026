"""
Módulo Principal (Orquestador y Entry Point)
Proyecto Final - Sistema de Gestión de Productos
Coordina la inicialización de la base de datos y el flujo del menú interactivo en consola.
"""

import conexion
import funciones

def mostrar_menu():
    """
    Despliega en pantalla el menú principal del sistema.
    Utiliza líneas divisorias calculadas con repetición de caracteres ("=" * 45).
    """
    print("\n" + "=" * 45)
    print("   SISTEMA DE GESTION DE PRODUCTOS")
    print("=" * 45)
    print("1. Registrar nuevo producto")
    print("2. Listar catalogo de productos")
    print("3. Buscar producto por ID")
    print("4. Actualizar datos de producto")
    print("5. Eliminar producto")
    print("6. Reporte de stock minimo")
    print("7. Salir del sistema")
    print("=" * 45)

def main():
    """
    Función principal de control.
    1. Verifica e inicializa la tabla en SQLite si no existe.
    2. Ejecuta el bucle continuo del menú hasta que el usuario elija la opción de salida.
    """
    # Inicialización preventiva: asegura que la base y tabla existan antes de operar
    conexion.crear_tabla()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-7): ").strip()

        # Estructura de control condicional para derivar la acción a funciones.py
        if opcion == "1":
            funciones.registrar_producto()
        elif opcion == "2":
            funciones.listar_productos()
        elif opcion == "3":
            funciones.buscar_producto()
        elif opcion == "4":
            funciones.actualizar_producto()
        elif opcion == "5":
            funciones.eliminar_producto()
        elif opcion == "6":
            funciones.reporte_stock()
        elif opcion == "7":
            print("\nGracias por utilizar el Sistema de Gestion. ¡Hasta luego!")
            break  # Finaliza el ciclo while y termina la ejecución
        else:
            print("\nError: Opcion no valida. Ingrese un numero del 1 al 7.")

# Punto de entrada estándar en Python: garantiza que main() solo corra al ejecutarse como script directo
if __name__ == "__main__":
    main()
