from collections import OrderedDict, Counter

def filtrar(data: dict):
    return set(data["compras"])-set(data["registrados"])

def eliminar_duplicados(data: dict):
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
    pass
    #resumen = {data["compras"][i]}

if __name__ == "__main__":
    data = {"compras": ["Luis", "Ana", "Luis", "Carlos", "Marta", "Ana", "Sofía", "Elena", "Luis", "Carlos"], 
                   "registrados": ["Ana", "Carlos", "Marta", "Elena"]}
    
    print(contar(data))
    #
