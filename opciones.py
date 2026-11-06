from auxiliares import limpiar_pantalla, es_duplicados, busqueda
# 1.
def cargar_herramientas(inventario:list): # carga uno o varios productos al sistema con su stock inicial
    while True:
        limpiar_pantalla()
        try: 
            cantidad = int(input("Ingrese la cantidad de herramientas que quiere cargar: "))
            if cantidad <= 0:
                raise ValueError("La cantidad a cargar no puede ser menor o igual a 0.")
        except ValueError as e: # atrapa el error en caso de que ocurra
            print(f"Error: {e}")
            input("Presione ENTER para reintentar...")
            continue # repite el bucle para que no continue la carga de datos
        break # sale del bucle solo cuando los datos son correctos

    for i in range(cantidad): # repite x veces que el usuario indique en el bucle anterior
        while True:
            limpiar_pantalla()
            try:
                nombre = input(f"Ingrese el nombre de la herramienta {i + 1}: ").strip() # strip() para borrar los espacios 
                if not nombre:
                    raise ValueError("Debe ingresar un nombre para la herramienta.")
                if es_duplicados(inventario,nombre): # verifica que la herramienta ya se encuentr en sistema
                    raise ValueError("La herramienta ya se encuentra disponible.")
            except ValueError as e: 
                print(f"Error: {e}")
                input("Presione ENTER para reintentar...")
                continue
            break

        while True:
            limpiar_pantalla()
            try:
                stock = int(input(f"Ingrese el stock inicial de {nombre}: "))
                if stock < 0:
                    raise ValueError("El stock inicial no puede ser menor a 0.")
            except ValueError as e:
                print(f"Error: {e}")
                input("Presione ENTER para reintentar...")
                continue
            break

        inventario.append({"herramienta":nombre,"cantidad":stock}) # agrega el diccionario a la lista
# 2.
def mostrar_inventario(inventario:list): # muestra el inventario actual
    if len(inventario) == 0: # en caso de que no haya en el inventario vuelve al menu
        print("El inventario esta vacio, no hay nada que mostrar.")
    else:
        print("-" * 25)
        print(f"{'LISTA DE HERRAMIENTAS':^25}") #^ para centrar el titulo y el numero reserva una cantidad de espacios 
        print("-" * 25)
        print(f"{'Herramienta':<15}{'Stock':>10}") #>< arrogan el texto para la izquierda o derecha
        print("-" * 25)
        for producto in inventario: # recorre los prodcutos y luego muestra el nombre y la cantidad
            print(f"{producto["herramienta"]:<15}{producto["cantidad"]:>10}")
        print("-" * 25)
    input("ENTER volver al menú...")
# 3.
def consultar_stock(inventario:list): #consulta el stock de un producto en especifico
    if len(inventario) == 0:
        print("El inventario está vacío, no hay nada que mostrar.")
        input("ENTER para volver al menú...")
    else:
        nombre = input("Ingrese el producto del cual quiere saber su stock: ").strip()  

        if not nombre:
            raise ValueError("El nombre del producto no puede estar vacío.") # devuelve un raise que atrapa main()

        producto = busqueda(inventario, nombre) # busca un producto y devuelve el diccionario en el que se encuentre

        if producto is not None: # verifica que se devuelva el diccionario
            print("-" * 25)
            print(f"{producto['herramienta']:<15}{producto['cantidad']:>10}")
            print("-" * 25)
        else:
            print("El producto no se encuentra en sistema.")

        input("ENTER para volver al menú...")
# 4.
def reporte_agotados(inventario: list): # busca si algun producto ya no tiene stock
    if len(inventario) == 0:
        print("El inventario está vacío, todavia no hay herramientas cargadas.")
    else:
        encontrado = False # bandera que cambia si se encuentra un productos en stock

        for producto in inventario:
            if producto["cantidad"] == 0: # compara la cantidad de cada producto con 0 
                if not encontrado:
                    print(f"{'PRODUCTOS AGOTADOS':^25}")
                    print("-" * 25)
                    encontrado = True

                print(producto["herramienta"]) # muestra el producto agotado
                print("-" * 25)

        if not encontrado:
            print("Ningún producto en el sistema se encuentra agotado.")

    input("ENTER para volver al menú...")
# 5.
def alta_producto(inventario:list): # ingresa un producto pero los raise los atrapa main()
    nombre = input("Ingrese el nombre de la herramienta : ").strip()
    if not nombre:
        raise ValueError("Debe ingresar un nombre para la herramienta.")
    if es_duplicados(inventario,nombre):
        raise ValueError("La herramienta ya se encuentra disponible.")
    try:
        stock = int(input(f"Ingrese el stock inicial de {nombre}: "))
    except ValueError:
        raise ValueError("El stock debe ser un numero entero.")
    if stock < 0:
        raise ValueError("El stock inicial no puede ser menor a 0.")

    inventario.append({"herramienta":nombre,"cantidad":stock})
    print("El producto se cargo en sistema correctamente!!!")
    input("ENTER para volver al menú...")
#6
def actualizar_stock(inventario:list): # modifica el stock de productos existentes 
    #Venta: disminuye el stock tras validar que hay unidades suficientes
    #Ingreso: aumenta el stock
    if len(inventario) == 0:
        print("El inventario está vacío, todavía no hay herramientas cargadas.")
        input("ENTER para volver al menú...")
    else:
        nombre = input("Ingrese el nombre del producto que quiere modificar su stock: ").strip()
        if not nombre: 
            raise ValueError ("El nombre del producto no puede estar vacío.") # devuelve raise que atrapa main()

        producto = busqueda(inventario, nombre) # busca un producto y devuelve el diccionario en el que se encuentre

        if producto is not None:
            operacion = input("Ingrese el tipo de movimiento, venta (1) o ingreso (2): ").strip()

            if operacion != "1" and operacion != "2": # vuelve al menu en caso de que se ingrese otra opcion 
                print("Opción incorrecta.")
                input("ENTER para volver al menú...")   
            else:
                try:
                    unidades = int(input("Ingrese la cantidad de stock para actualizar: "))
                except ValueError: # devuelve los errores de int() a main() pero con un msj personalizado 
                    raise ValueError("Las unidades deben ser un número entero.") 
                
                if unidades <= 0:
                    raise ValueError("Las unidades del movimiento deben ser mayores que 0.")

                if operacion == "1":
                    if producto["cantidad"] < unidades: # verifica que lo restado no sea mayor a lo disponible
                        raise ValueError("No hay stock suficiente para realizar la venta.")
                    producto["cantidad"] = producto["cantidad"] - unidades # disminuye el valor del stock
                    print("La venta se ha realizado correctamente!!!") # avisa de la venta
                else:
                    producto["cantidad"] = producto["cantidad"] + unidades # aumenta el valor del stock
                    print("La mercadería nueva fue agregada al sistema correctamente!!!") # avisa de la nueva mercaderia agregada
                
                input("ENTER para volver al menú...")

        else:
            print("El producto no se encuentra en inventario.")
            input("ENTER para volver al menú...")
