from tienda import Tienda

#Funcion de validacion de numero flotante
def es_flotante(num: str):
    """
    Funcion que toma una cadena de texto y valida si se trata de un numero flotante.

    Parameters:
        num (String): La cadena de texto a evaluar.
    
    Returns:
        Boolean == True: Si num es un numero flotante.
        Boolean == False: Si num no es un numero flotante.
    """
    #Se valida cadena vacia
    if num == "":
        return False
    #Se agrega bandera de validacion de caracter numerico
    bandera = False
    #Se agrega contador de puntos decimales
    contador = 0
    #Se agrega contador de guiones
    guion = -1
    if (num[0] == "-"):
        guion += 1
    #Ciclo de validacion de digitos y contador de puntos decimales
    for x in num:
        #Se valida digito y un unico punto decimal
        if x in "1234567890":
            bandera = True
        elif x == "." and contador < 1:
            #Se cuentan puntos
            contador += 1
        elif x == "-" and guion < 1:
            #Se cuentan guiones
            guion += 1
        else:
            return False
    #Se valida la existencia de al menos un numero y/o el guion de negativo
    return True if bandera and (guion == 1 or guion == -1) else False

def pedir_campo(nombre: str, condicion = str):
    while True:
        print(f"\nIngrese {nombre}:")
        x = input()
        if condicion(x):
            return x

def menu(tienda: Tienda):
    while True:
        parte_menu = ["salir.", "agregar un cliente nuevo.", "agregar un producto nuevo.", "registrar una venta.", 
                      "obtener un resumen de un cliente."]
        print(f"\n----Menu de la tienda {tienda.nombre}----\nPresione la tecla entre []:")
        for x in [f"[{i}] : Para {parte_menu[i]}" for i in range(len(parte_menu))]:
            print(x)
        entrada = input()
        match entrada:
            case "1":
                tienda.registrar_cliente(
                    pedir_campo("nombre del cliente", lambda x: (x.replace(" ", "") != "") and x not in tienda.clientes.keys()), 
                    pedir_campo("correo electronico", lambda x: (x.count("@") == 1) and (x.count(".") != 0)),
                    float(pedir_campo("saldo", es_flotante))
                )
            case "2":
                tienda.registrar_producto(
                    pedir_campo("nombre del producto", lambda x: (x.replace(" ", "") != "") and x not in tienda.productos.keys()),
                    float(pedir_campo("precio", es_flotante))
                )
            case "3":
                no_clientes = len(tienda.clientes.keys())
                no_productos = len(tienda.productos.keys())
                print(no_clientes, no_productos)
                if no_clientes != 0 and no_productos != 0:
                    cliente = pedir_campo("nombre del cliente", lambda x: (x.replace(" ", "") != "") and x in tienda.clientes.keys())
                    lista_compras = []
                    while True:
                        lista_compras.append(
                            tienda.productos[pedir_campo("nombre del producto", lambda x: (x.replace(" ", "") != "") and x in tienda.productos.keys())]
                            )
                        if pedir_campo(" [S] para añadir otro producto, cualquier otra tecla para volver al menu", lambda x: x.lower() in "s").lower() != "s":
                            break
                    tienda.registrar_venta(cliente, lista_compras)
                else:
                    print(f"\nFaltan {"clientes "*(not bool(no_clientes)) + "y "*((not bool(no_clientes) and not bool(no_productos))) + "productos "*(not bool(no_productos))}intente agregando algunos.")
            case "4":
                cliente = (pedir_campo("cliente", lambda x: x in tienda.clientes.keys()) if len(tienda.clientes.keys()) != 0 else "")
                tienda.mostrar_resultado(cliente)
            case "0":
                break

if __name__ == "__main__":
    tienda = Tienda(pedir_campo("el nombre de la tienda"))
    tienda.mostrar_resultado()
    menu(tienda)
