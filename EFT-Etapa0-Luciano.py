import os, time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_opc():
        try: 
        return opc > 0 and opc < 8
    except ValueError:
        print('Error, debe ser un numero entero desde el 1 al 7')

def leer_opc():
    try:
        opc = int(input('Ingrese una opcion valida: '))
        if not validar_opc(opc):
            print('Error, opcion no valida, reintente') 
            return
    except ValueError: 
        print('Error, debe ser un numero entero desde el 1 al 7')

def stock_categoria():
    pass

def validar_rango():
    pass

def buscar_rango_precio():
    pass

def validar_actualizacion():
    pass

def actualizar_precio():
    pass

def validar_codigo(codigo):
    pass

def validar_nombre(nombre):
    pass

def validar_categoria(categoria, productos, inventario):
    toal = 0
    for llave, valor in productos.item():
        if llave[1].lower == categoria.lower():
            total += inventario[llave][0]
    if total > 0 :
        print(f'Stock total de {categoria.lower().capitalize()} = {total}')
    elif total == 0:
        print(f'No hay stock de {categoria.lower().capitalize()}')
    else:
        print('Categoria inexistente')
        return

def validar_precio(precio):
    pass

def validar_disponible(opcion):
    return disponible.lower in ('s', 'n')
    disponible =disponible.strip().lower()
    if disponible == 's':
        return True
    elif disponible == 'n':
        return False
    else:
        return -1

def validar_stock(stock):
    pass

def validar_vendidos(vendidos):
    pass

def agregar_producto():
    pass

def eliminar_producto():
    pass

def mostrar_productos():
    pass

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
    productos = {
        'P101': ['Cuaderno', 'Papeleria', 2490, True],
        'P102': ['Lapiz', 'Papeleria', 590, False]
    }
    inventario = {
        'P101': [30, 15],
        'P102': [120, 50]
    }
    while True:
        clear()
        menu()
        leer_opc()
        if opc == 7:
            clean()
            print('Gracias por usar este programa')
            time.sleep(2)
            break
        elif opc == 1:
            clean()
            categoria = input('Ingrese la categoria a verificar: ')
            if not validar_categoria(categoria):
                print('La categoria no puede quedar vacia')
                return
            else:
                validar_categoria(categoria, productos, inventario)
        elif opc == 2:
            clean()
            print('saygex')
        elif opc == 3:
            clean()
            print('saygex')
        elif opc == 4:
            clean()
            print('saygex')
        elif opc == 5:
            clean()
            print('saygex')
        elif opc == 6:
            clean()
            print('saygex')
 
main()

