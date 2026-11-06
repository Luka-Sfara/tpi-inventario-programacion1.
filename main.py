from opciones import (cargar_herramientas, mostrar_inventario, consultar_stock,
                      reporte_agotados, alta_producto, actualizar_stock)
from auxiliares import limpiar_pantalla

def mostrar_menu(): # interfaz para ver las opciones
    print("=" * 35)
    print(f"{'CONTROL DE INVENTARIO':^35}") #^35 centra el str y reserva esa cantidad de espacios
    print("=" * 35)
    print("1. Cargar herramientas")
    print("2. Mostrar inventario")
    print("3. Consultar stock")
    print("4. Reporte de agotados")
    print("5. Alta de nuevo producto")
    print("6. Actualizar stock (venta / ingreso)")
    print("7. Salir")
    print("=" * 35)


def main(): # funcion pricipal que ejecuta todo el programa
    inventario = []
    opcion = 0

    while opcion != 7: # sigue hasta que el usuario ingrese 7
        limpiar_pantalla() # funcion auxiliar que limpia la terminal
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            elif opcion != 7:
                raise ValueError("Opción fuera de rango (1 a 7).") # valida que no se ingresen opciones erroneas
        except ValueError as e: # atrapa los errores dentro de las funciones y las muestras
            print(f"Error: {e}")
            input("ENTER para volver al menú...")

    print("Sistema finalizado.")


main() 