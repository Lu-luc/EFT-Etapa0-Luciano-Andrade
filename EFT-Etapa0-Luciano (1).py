import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_opc():
    try: 
        return opc > 0 and opc < 8
    except ValueError:
        print('Error, debe ser un numero entero desde el 1 al 7')

def leer_opc (opc):
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

def validar_categoria(categoria):
    pass

def validar_precio(precio):
    pass

def validar_disponible(opcion):
    pass

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
    pass

def main():
    clear()
    menu()
    opc = leer_opc()

main()

