import time

from libsss import validar_nombre
from libsss import validar_dni

def menu():
    """Menu de Opciones del menu principal"""
    print("=".center(50,'='))
    print("Restaurante Astrid & Gastón".center(50,' '))
    print("MENU".center(50,' '))
    print("=".center(50,'='))
    print('    A | Comida Mediterranea')
    print('    B | Comida Criolla')
    print('    C | Comida Marina')
    print('    D | Salir')
    print("=".center(50,'='))

def mediterranea():
    """Menu de Opciones de Comida  Mediterranea"""
    print()
    print("COMIDA MEDITERRANEA".center(50,' '))
    print("=".center(50,'='))
    print('    A | Briami griego     |s/ 34.50')
    print('    B | Bruschetta        |s/ 55.00')
    print('    C | Falafel           |s/ 42.00')
    print('    D | Mudammas          |s/ 38.00')
    print('    E | Fattoush          |s/ 52.00')
    print('    F | Ratatouille       |s/ 37.00')
    print('    G | Spanakopita       |s/ 29.00')
    print('    J | ========== Salir =========')
    print("=".center(50,'='))

def criolla():
    """Menu de Opciones de Comida Criolla"""
    print()
    print("COMIDA CRIOLLA".center(50,' '))
    print("=".center(50,'='))
    print('    A | Tallarines Rojo     |s/ 14.50')
    print('    B | Caldo de Gallina    |s/ 15.00')
    print('    C | Arroz con Pato      |s/ 19.00')
    print('    D | Seco de Pollo       |s/ 18.00')
    print('    E | Lomo Saltado        |s/ 17.00')
    print('    F | Lentejas            |s/ 17.00')
    print('    G | Tallarin Saltado    |s/ 17.00')
    print('    J | =========== Salir ===========')
    print("=".center(50,'='))


def marina():
    """Menu de Opciones de Comida Marina"""
    print()
    print("COMIDA MARINA".center(50,' '))
    print("=".center(50,'='))
    print('    A | Lomo de Robalo       |s/ 92.50')
    print('    B | Cebiche clásico      |s/ 87.50')
    print('    C | Tiradito de Lenguado |s/ 69.00')
    print('    D |=========== SALIR =============')
    print("=".center(50,'='))

def detalle_pedido(listado_platos_pedido,precio_platos_pedido):
    """lista los platos y los subtotales"""
    for i, (plato, precio) in enumerate(zip(listado_platos_pedido, precio_platos_pedido), start=1):
        print(f"{i}. {plato}  S/.:{precio: >5}")

def option_d (subtotal,listado_platos_pedido,precio_platos_pedido):
    """Function printing python version."""    
    if subtotal>0:
        print("=".center(50,'='))
        print("Restaurante Astrid & Gastón".center(50,' '))
        print("Cliente".center(50,' '))
        print("=".center(50,'='))
        nombres=validar_nombre()
        dni=validar_dni()
        print("=".center(50,'='))
        print("BOLETA DE VENTA ELECTRONICA".center(50,' '))
        print("=".center(50,'='))
        print("Fecha y hora : " + time.strftime("%c"))
        print("DNI : " + str(dni))
        print("Cliente : " + str(nombres))
        print("=".center(50,'='))
        print("DETALLE DE VENTA".center(50,' '))
        print("=".center(50,'='))
        detalle_pedido(listado_platos_pedido,precio_platos_pedido)
        print("=".center(50,'='))
        print(f' Subtotal  S/.    : {subtotal}')
        print(f' I.G.V. 18.00 S/. : {round(subtotal*0.18,2)}')
        print(' Importe Total S/.: ' +str(subtotal+(subtotal*0.18)))
        print()
        print("Gracias por su Compra!".center(50,' '))         
    else:
        print("No se a registrado ninguna compra , GRACIAS POR SU ATENCION")


def main():
    """Function principal"""
    subtotal = 0
    listado_platos_pedido = []
    precio_platos_pedido = []
    while True :
        menu()
        sub1=input("Seleccione un Item : ").upper()
        print()

        if sub1 == "A":
            while True:
                mediterranea()
                letra_mediterranea=input("Seleccione un LETRA : ").upper()
                if letra_mediterranea =="A":
                    subtotal=34.50+subtotal
                elif letra_mediterranea =="B":
                    subtotal=55+subtotal                 
                elif letra_mediterranea =="C":
                    subtotal=42+subtotal
                elif letra_mediterranea =="D":
                    subtotal=38+subtotal
                elif letra_mediterranea =="E":
                    subtotal=52+subtotal
                elif letra_mediterranea =="F":
                    subtotal=37+subtotal
                elif letra_mediterranea =="G":
                    subtotal=29+subtotal 
                elif letra_mediterranea =="J":
                    print("----OK GRACIAS----")
                    break
                else:
                    print("---Esa opcion no se encuentra disponible solo ingrese las LETRAS DISPONIBLES---")
                print("OK algo mas desea pedir ?")

        
        elif sub1 == "B": 
                
            while True:
                
                criolla()
                letra_criolla=input("Seleccione un LETRA : ").upper()
                if letra_criolla =="A":
                           
                    subtotal=14.50+subtotal
                elif letra_criolla =="B":
                    subtotal=15+subtotal
                elif letra_criolla =="C":
                    subtotal=19+subtotal
                elif letra_criolla =="D":
                    subtotal=18+subtotal
                elif letra_criolla =="E":
                    subtotal=17+subtotal
                elif letra_criolla =="F":
                    subtotal=17+subtotal
                elif letra_criolla =="G":
                    subtotal=17+subtotal
                elif letra_criolla =="J":
                    print("---OK GRACIAS---")
                  
                    break
                else:
                    print("Esa opcion no se encuentra disponible solo ingrese las LETRAS DISPONIBLES")
                print("OK algo mas desea pedir ?")
        
        elif sub1 == "C":
            inv = {
                'A' : {'nombre':'Lomo de Robalo','precio': 92.50},
                'B' : {'nombre':'Cebiche clásico','precio': 87.50},
                'C' : {'nombre':'Tiradito de Lenguado','precio': 69.00},
            }

            while True:
                marina()
                letra_marina=input("Seleccione un LETRA : ").upper()
                if letra_marina in inv:
                    subtotal += inv[letra_marina]['precio']
                    listado_platos_pedido.append(inv[letra_marina]['nombre'])
                    precio_platos_pedido.append(inv[letra_marina]['precio'])
                   

                elif letra_marina =="D":
                    print("---OK GRACIAS---")
                    break
                else:
                    print("Esa opcion no se encuentra disponible solo ingrese las LETRAS DISPONIBLES")
                print("OK algo mas desea pedir ?")

        #ahora la opcion de la boleta
        elif sub1=="D":
            option_d(subtotal,listado_platos_pedido,precio_platos_pedido)
            break
            
        else:
            print("OPCION NO DISPONIBLE INTENTE DE NUEVO")


if __name__=="__main__":
    main()