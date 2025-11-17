#Se importan liberias
from collections import OrderedDict, Counter

#Funcion de filtrado de ambas listas
def filtrar(data: dict):
    """
    Funcion que toma un diccionario y entrega un conjunto de registros que estan en la key 'compras' y no en 'registrados'

    Parameters:
        data (Dictionary): Diccionario con claves ('compras', 'registrados') representando listas de clientes.
    
    Returns:
        (Set): Conjunto de nombres de clientes.
    """
    #Se retorna la diferencia de conjuntos sin repeticiones
    return set(data["compras"])-set(data["registrados"])

#Funcion de eliminacion de duplicados (ordenado)
def eliminar_duplicados(data: dict):
    """
    Funcion que toma un diccionario y entrega un OrderedDict con los registros ordenados por insercion y sin repeticion

    Parameters:
        data (Dictionary): Diccionario con claves ('compras', 'registrados') representando listas de clientes.
    
    Returns:
        dic (OrderedDict): Diccionario ordenado de clientes no repetidos.
    """
    #Se inicializa un OrderedDict y un contador en 0
    dic = OrderedDict()
    #Ciclo de deteccion de compradores unicos
    for x in data["compras"]:
        #Si el comprador no ha sido añadido al diccionario se añade
        if x not in dic.keys():
            #Se agrega el comrpador
            dic[x] = len(dic)
    #Se regresa el diccionario ordenado
    return dic

#Funcion para contar frecuencia de compra
def contar(data: dict):
    """
    Funcion que toma un diccionario y entrega un diccionario con la cantidad de repeticiones por cada registro según la lista de compras.

    Parameters:
        data (Dictionary): Diccionario con claves ('compras', 'registrados') representando listas de clientes.
    
    Returns:
        (Dictionary): Diccionario de clientes por frecuencia de aparicion.
    """
    #Se regresa el diccionario de frecuencia
    return Counter(data["compras"])

#Funcion para generar un diccionario con un resumen de clientes frecuentes (mas de una compra)
def resumir(data: dict):
    """
    Funcion que toma un diccionario y entrega un diccionario con la cantidad de compras en texto por cada comprador.

    Parameters:
        data (Dictionary): Diccionario con claves ('compras', 'registrados') representando listas de clientes.
    
    Returns:
        (Dictionary): Diccionario de clientes por frecuencia de aparicion y mensaje de compra. Se cuentan sólo aquellos mayores a uno en frecuencia.
    """
    #Se obtiene el diccionario de frecuencia de compras
    compras = contar(data)
    #Se genera por comprension un diccionario con leyendas de compra para clientes frecuentes
    return {x : f"Ha comprado {compras[x]} veces" for x in data["compras"] if compras[x] > 1}

#Funcion para generar impresion de mensaje y datos en un iterable
def imprimir_bloque(mensaje: str, data):
    """
    Funcion que toma un iterable de datos y un mensaje para generar una impresión ordenada de los datos contenidos.

    Parameters:
        mensaje (String): Representa un mensaje previo a la impresion de los datos del conjunto.
        data (Any): Iterable coordenado que representa el conjunto de datos.
    
    Returns:
        None: No retorna nada.
    """
    #Se imprime mensaje personalziado
    print(f"\n{mensaje}")
    #Ciclo para recorrer el iterable
    for x in data:
        #Se imprimen los datos según sea un set de datos o un diccionario
        print(x) if type(data) == set else print(f"{data[x]} : {x}")

#Funcion de arranque
if __name__ == "__main__":
    #Se inicializan los datos segun las claves 'compras' y 'registrados'
    data = {"compras": ["Luis", "Ana", "Luis", "Carlos", "Marta", "Ana", "Sofía", "Elena", "Luis", "Carlos"], 
            "registrados": ["Ana", "Carlos", "Marta", "Elena"]}
    #Se genera la impresion del primer bloque
    imprimir_bloque("Clientes nuevos no registrados:", filtrar(data))
    #Se genera la impresion del segundo bloque
    imprimir_bloque("Lista de clientes únicos:", eliminar_duplicados(data))
    #Se genera la impresion del tercer bloque
    imprimir_bloque("Resumen por cliente frecuente:", resumir(data))
