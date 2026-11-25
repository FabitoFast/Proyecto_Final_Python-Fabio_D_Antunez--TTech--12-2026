import conexion
import funciones

def mostrar_menu():
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
    conexion.crear_tabla()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-7): ").strip()
        
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
            break
        else:
            print("\nError: Opcion no valida. Ingrese un numero del 1 al 7.")

if __name__ == "__main__":
    main()
