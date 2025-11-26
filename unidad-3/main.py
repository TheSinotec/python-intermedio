#Se importa la clase Tienda del modulo tienda
from tienda import Tienda

#Funcion de validacion de numero flotante
def es_flotante(num: str):
    """
    Funcion que toma una cadena de texto y valida si se trata de un numero flotante positivo.

    Parameters:
        num (String): La cadena de texto a evaluar.
    
    Returns:
        Boolean == True: Si num es un numero flotante positivo.
        Boolean == False: Si num no es un numero flotante positivo.
    """
    #Se valida cadena vacia
    if num == "":
        return False
    #Se agrega bandera de validacion de caracter numerico
    bandera = False
    #Se agrega contador de puntos decimales
    contador = 0
    #Ciclo de validacion de digitos y contador de puntos decimales
    for x in num:
        #Se valida digito y un unico punto decimal
        if x in "1234567890":
            bandera = True
        elif x == "." and contador < 1:
            #Se cuentan puntos
            contador += 1
        else:
            return False
    #Se valida la existencia de al menos un numero
    return True if bandera else False

#Funcion para pedir campos de texto
def pedir_campo(nombre: str, condicion = str):
    """
    Funcion que muestra un mensaje de captura y una funcion de validacion booleana.

    Parameters:
        nombre (String): El mensaje de ingreso.
        condicion (Function): Funcion de validacion booleana.
    
    Returns:
        x (String): El texto capurado y validado.
    """
    #Bucle de validación
    while True:
        #Texto de entrada
        print(f"\nIngrese {nombre}:")
        #Ingreso por teclado
        x = input()
        #Condicion aplicada a la entrada
        if condicion(x):
            #Si la condicion es valida se retorna el valor
            return x

#Funcion de menu de opciones
def menu(tienda: Tienda):
    """
    Funcion de ejecucion del menu de la tienda.

    Parameters:
        tienda (Tienda): El objeto Tienda, que representa el manejo de la informacion.
    
    Returns:
        (None): No regresa nada.
    """
    #Se inicializa una lista con las secciones del menu
    parte_menu = ["salir.", "agregar un cliente nuevo.", "agregar un producto nuevo.", "registrar una venta.", "obtener un resumen de un cliente."]
    #Bucle de validacion
    while True:
        #Se imprime un mensaje de bienvenida
        print(f"\n----Menu de la tienda {tienda.nombre}----\nPresione la tecla entre []:")
        #Se generan las opciones del menú
        for x in [f"[{i}] : Para {parte_menu[i]}" for i in range(len(parte_menu))]:
            #Se imprime la opcion
            print(x)
        #Se pide una opcion
        entrada = pedir_campo("una opcion")
        #Se valida la opcion elegida
        match entrada:
            #Caso para registrar nuevo cliente
            case "1":
                #Se registra un cliente pidiendo y validando cada campo
                tienda.registrar_cliente(
                    #Se pide nombre de cliente
                    pedir_campo("nombre del cliente", lambda x: (x.replace(" ", "") != "") and x not in tienda.clientes.keys()), 
                    #Se pide correo del cliente
                    pedir_campo("correo electronico", lambda x: (x.count("@") == 1) and (x.count(".") != 0)).lower(),
                    #Se pide el saldo de cliente
                    float(pedir_campo("saldo", es_flotante))
                )
            #Caso para registrar nuevo producto
            case "2":
                #Se registra un producto pidiendo y validando cada campo
                tienda.registrar_producto(
                    #Se pide nombre del producto
                    pedir_campo("nombre del producto", lambda x: (x.replace(" ", "") != "") and x not in tienda.productos.keys()),
                    #Se pide el precio del producto
                    float(pedir_campo("precio", es_flotante))
                )
            #Caso para registrar una venta
            case "3":
                #Se guarda la cantidad de clientes
                no_clientes = len(tienda.clientes.keys())
                #Se guarda la cantidad de productos
                no_productos = len(tienda.productos.keys())
                #Se valida que haya clientes y productos
                if no_clientes != 0 and no_productos != 0:
                    #Se obtiene el cliente que compra
                    cliente = pedir_campo("nombre del cliente", lambda x: (x.replace(" ", "") != "") and x in tienda.clientes.keys())
                    #Se genera una lista de compras
                    lista_compras = []
                    #Ciclo para acumular compras
                    while True:
                        #Se suman productos a la lista
                        lista_compras.append(
                            #Se obtiene el producto deseado
                            tienda.productos[pedir_campo("nombre del producto", lambda x: (x.replace(" ", "") != "") and x in tienda.productos.keys())]
                            )
                        #Validacion de escape
                        if pedir_campo("[S] para añadir otro producto, cualquier otra tecla para volver al menu").lower() != "s":
                            #Escape
                            break
                    #Se registra la venta
                    tienda.registrar_venta(cliente, lista_compras)
                else:
                    #Se manda mensaje cuando no hay clientes y/o productos
                    print(f"\nFaltan {"clientes "*(not bool(no_clientes)) + "y "*((not bool(no_clientes) and not bool(no_productos))) + "productos "*(not bool(no_productos))}intente agregando algunos.")
            #Caso para obtener informacion
            case "4":
                #Se obtiene el nombre del cliente
                cliente = (pedir_campo("cliente", lambda x: x in tienda.clientes.keys()) if len(tienda.clientes.keys()) != 0 else "")
                #Se muestra la informacion 
                tienda.mostrar_resultado(cliente)
            #Caso para escape del menu
            case "0":
                #Escape
                break

#Funcion de arranque
if __name__ == "__main__":
    #Se inicializa una tienda pidiendo el nombre
    tienda = Tienda(pedir_campo("el nombre de la tienda"))
    #Se inicia el menu de tienda
    menu(tienda)
