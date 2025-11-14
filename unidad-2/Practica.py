#Se importan liberias
from collections import OrderedDict, Counter

def filtrar(data: dict):
    """
    Función que toma un diccionario y entrega un conjunto de registros que estan en la key 'compras' y no en 'registrados'

    Parameters:
        data (Dictionary): Diccionario con claves ('compras', 'registrados') representando listas de clientes.
    
    Returns:
        (Set): Conjunto de nombres de clientes.
    """
    return set(data["compras"])-set(data["registrados"])

def eliminar_duplicados(data: dict):
    """
    Función que toma un diccionario y entrega un OrderedDict con los registros ordenados por insercion y sin repeticion

    Parameters:
        data (Dictionary): Diccionario con claves ('compras', 'registrados') representando listas de clientes.
    
    Returns:
        dic (OrderedDict): Diccionario ordenado de clientes no repetidos.
    """
    dic = OrderedDict()
    i = 0
    while i < len(set(data["compras"])):
        if data["compras"][i] not in dic.keys():
            dic[data["compras"][i]] = len(dic)
        i+=1
    return dic

def contar(data: dict):
    return Counter(data["compras"])

def resumir(data: dict):
    compras = contar(data)
    return {x : f"Ha comprado {compras[x]} veces" for x in data["compras"] if compras[x] > 1}

def imprimir_bloque(mensaje: str, data):
    print(f"\n{mensaje}")
    for x in data:
        print(x) if type(data) == set else print(f"{data[x]} : {x}")

if __name__ == "__main__":
    data = {"compras": ["Luis", "Ana", "Luis", "Carlos", "Marta", "Ana", "Sofía", "Elena", "Luis", "Carlos"], 
                   "registrados": ["Ana", "Carlos", "Marta", "Elena"]}
    

    imprimir_bloque("Clientes nuevos no registrados:", filtrar(data))
    imprimir_bloque("Lista de clientes únicos:", eliminar_duplicados(data))
    imprimir_bloque("Resumen por cliente frecuente:", resumir(data))
