import os, time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def leer_opcion():
    """Valida mediante manejo de excepciones que sea un entero entre 1 y 7"""
    try:
        opcion = int(input("Seleccione una opción (1-7): "))
        if 1 <= opcion <= 7:
            return opcion
        else:
            print("Debe seleccionar una opción válida")
            return None
    except ValueError:
        print("Debe seleccionar una opción válida")
        return None

def stock_categoria(categoria, productos, inventario):
    total_stock = 0
    encontrado = False
    for codigo, datos in productos.items():
        if datos[1].lower() == categoria.lower():
            encontrado = True
            total_stock += inventario[codigo][0]
    if encontrado:
        print(f"\n stock total para la categoría '{categoria}' es: {total_stock}")
    else:
        print(f"\nNo se encontraron productos en la categoría '{categoria}'")

    
def buscar_precio(precio_min, precio_max, productos, inventario):
    resultados = []
    
    for codigo, datos in productos.items():
        nombre = datos[0]
        precio = datos[2]
        stock = inventario[codigo][0]
        
        if precio_min <= precio <= precio_max and stock > 0:
            resultados.append((nombre, codigo))
            
    resultados.sort()
    
    print(f"\nProductos entre ${precio_min} y ${precio_max} con stock disponible:")
    if not resultados:
        print("No se encontraron productos que cumplan los criterios.")
    else:
        for nombre, codigo in resultados:
            print(f"{nombre}--{codigo}")

def buscar_codigo(codigo, productos):
    for llave in productos:
        if llave.lower() == codigo.lower():
            return True
    return False

def actualizar_precio(codigo, nuevo_precio, productos):
    for llave in productos:
        if llave.lower() == codigo.lower():
            productos[llave][2] = nuevo_precio
            return True
    return False

def validar_codigo(codigo, productos):
    if not codigo or codigo.strip() == "":
        return False
    for llave in productos:
        if llave.lower() == codigo.lower():
            return False
    return True

def validar_nombre(nombre):
    if not nombre or nombre.strip() == "":
        return False
    return True
    
def validar_categoria(categoria):
    if not categoria or categoria.strip() == "":
        return False
    return True

def validar_precio(precio):
    return precio > 0

def validar_disponible(opcion):
    return opcion.lower() in ['s', 'n']

def validar_stock(stock):
    return stock >= 0

def validar_vendidos(vendidos):
    return vendidos >= 0

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    if not validar_codigo(codigo, productos):
        return False
    estado_disponible = True if disponible.lower() == 's' else False
    productos[codigo] = [nombre, categoria, precio, estado_disponible]
    inventario[codigo] = [stock, vendidos]
    return True

def eliminar_producto(codigo, productos, inventario):
    llave_a_eliminar = None
    for llave in productos:
        if llave.lower() == codigo.lower():
            llave_a_eliminar = llave
            break
    if llave_a_eliminar:
        del productos[llave_a_eliminar]
        del inventario[llave_a_eliminar]
        return True
    return False

def mostrar_productos(productos, inventario):
    if not productos:
        print("\nNo hay productos registrados en el sistema.")
        return
        
    for codigo in productos:
        print(f"\nCODIGO: {codigo}")
        print(f"Nombre: {productos[codigo][0]}")
        print(f"Categoría: {productos[codigo][1]}")
        print(f"Precio: ${productos[codigo][2]}")
        print(f"Disponible: {productos[codigo][3]}")
        print(f"Stock: {inventario[codigo][0]}")
        print(f"Vendidos: {inventario[codigo][1]}")

def menu():
    print('|=========================================|')
    print('|                 Main Menu               |')
    print('|=========================================|')
    print('| 1 | Buscar Stock por Categoria          |')
    print('| 2 | Buscar Porducto por rango de precio |')
    print('| 3 | Actualizar precio                   |')
    print('| 4 | Agregar producto                    |')
    print('| 5 | Eliminar producto                   |')
    print('| 6 | Mostrar productos                   |')
    print('| 7 | Salir                               |')
    print('|=========================================|')

def main():
    # Inicialización local de estructuras (Datos de prueba del PDF)
    productos = {
        "P101": ["Cuaderno", "Papelería", 2490, True],
        "P102": ["Lápiz", "Papelería", 590, True],
        "P103": ["Botella", "Accesorios", 6990, False],
        "P104": ["Mochila", "Accesorios", 24990, True]
    }
    
    inventario = {
        "P101": [30, 15],
        "P102": [120, 50],
        "P103": [0, 10],
        "P104": [8, 25]
    }

    while True:
        clear()
        menu()
        opcion = leer_opcion()
        
        if opcion is None:
            continue
            
        if opcion == 1:
            categoria = input("Ingrese la categoría a buscar: ")
            stock_categoria(categoria, productos, inventario)
            
        elif opcion == 2:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                if p_min >= 0 and p_max >= p_min:
                    buscar_precio(p_min, p_max, productos, inventario)
                else:
                    print("Error: Rangos de precios inválidos.")
            except ValueError:
                print("Error: Los precios deben ser números enteros.")
                
        elif opcion == 3:
            continuar = 's'
            while continuar.lower() == 's':
                codigo = input("Ingrese el código del producto a actualizar: ")
                if buscar_codigo(codigo, productos):
                    try:
                        nuevo_precio = int(input("Ingrese el nuevo precio: "))
                        if validar_precio(nuevo_precio):
                            actualizar_precio(codigo, nuevo_precio, productos)
                            print("Precio actualizado con éxito.")
                        else:
                            print("Error: El precio debe ser mayor a cero.")
                    except ValueError:
                        print("Error: Entrada inválida, debe ser un número entero.")
                else:
                    print("Código inexistente")
                
                continuar = input("¿Desea actualizar otro precio? (s/n): ")
                
        elif opcion == 4:
            print("\n--- Registrar Nuevo Producto ---")
            
            codigo = input("Código: ")
            if not validar_codigo(codigo, productos):
                print("Error: Código vacío o ya existente.")
                continue
                
            nombre = input("Nombre: ")
            if not validar_nombre(nombre):
                print("Error: El nombre no puede estar vacío.")
                continue
                
            categoria = input("Categoría: ")
            if not validar_categoria(categoria):
                print("Error: La categoría no puede estar vacía.")
                continue
                
            try:
                precio = int(input("Precio: "))
                if not validar_precio(precio):
                    print("Error: El precio debe ser un entero mayor que cero.")
                    continue
            except ValueError:
                print("Error: Debe ingresar un número entero.")
                continue
                
            disponible = input("¿Disponible? (s/n): ")
            if not validar_disponible(disponible):
                print("Error: Debe ingresar 's' o 'n'.")
                continue
                
            try:
                stock = int(input("Stock inicial: "))
                if not validar_stock(stock):
                    print("Error: El stock debe ser mayor o igual a cero.")
                    continue
            except ValueError:
                print("Error: Debe ingresar un número entero.")
                continue
                
            try:
                vendidos = int(input("Cantidad vendidos inicial: "))
                if not validar_vendidos(vendidos):
                    print("Error: Los vendidos deben ser mayor o igual a cero.")
                    continue
            except ValueError:
                print("Error: Debe ingresar un número entero.")
                continue
            exito = agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario)
            if exito:
                print("¡Producto agregado exitosamente!")
            else:
                print("Ocurrió un error al intentar agregar el producto.")
                
        elif opcion == 5:
            codigo = input("Ingrese el código del producto a eliminar: ")
            if eliminar_producto(codigo, productos, inventario):
                print("¡Producto eliminado exitosamente!")
            else:
                print("Error: El código no existe.")
                
        elif opcion == 6:
            mostrar_productos(productos, inventario)
            
        elif opcion == 7:
            print("Saliendo del sistema. ¡Hasta pronto!")
main()

