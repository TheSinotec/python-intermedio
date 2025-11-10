#Se importan liberias
import time
import functools

def medir_tiempo(funcion):
    def wrapper():
        inicio = time.time()
        funcion()
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos.\n")
    return wrapper

def auditar_funcion(funcion):
    dic = {"filtrado": 0, "transformar": 0, "ordenar": 0, "reducir": 0, "lista_original": 0}
    def wrapper():
        dic[funcion.__name__] += 1
        print(f"\nLa función '{funcion.__name__}' se está ejecutando...")
        funcion()
        print(f"Se ha ejecutado {dic[funcion.__name__]} ve{"z" if dic[funcion.__name__] == 1 else "ces"}.")
    return wrapper

def leer_temperaturas():
    ciudades = [('Estado de México', 50), ('Nuevo León', 71), ('Tamaulipas', 77), ('Coahuila', 79), ('Jalisco', 81), ('Veracruz', 84), ('Guanajuato', 85), ('Sonora', 87), ('Baja California', 88), ('Chiapas', 90), ('Colima', 92), ('Michoacán', 93), ('Morelos', 95), ('Quintana Roo', 96), ('Sinaloa', 97), ('Baja California Sur', 0), ('Campeche', 1), ('Chihuahua', 4), ('Durango', 6), ('Guerrero', 7), ('Puebla', 9), ('Querétaro', 11), ('San Luis Potosí', 12), ('Aguascalientes', 13), ('Hidalgo', 14), ('Mexico City', 17), ('Nayarit', 19), ('Oaxaca', 20), ('Tabasco', 21), ('Yucatán', 22), ('Zacatecas', 24), ('Tlaxcala', 25)]
    for x in ciudades:
        yield x

@medir_tiempo
@auditar_funcion
def filtrado():
    for x in list(filter(lambda x: x[1] >= 30, leer_temperaturas())):
        print(f"{x[0]}: {x[1]}")

@medir_tiempo
@auditar_funcion
def transformar():
    for x in list(map(lambda x: f"Alerta de calor en {x[0]}: {x[1]}°C", leer_temperaturas())):
        print(x)

@medir_tiempo
@auditar_funcion
def ordenar():
    for x in sorted(leer_temperaturas(), key=lambda x: x[1], reverse = True):
        print(f"{x[0]}: {x[1]}")

@medir_tiempo
@auditar_funcion
def reducir():
    print(f"Temperatura promedio de alertas: {functools.reduce(lambda x, y:  x + y, temp := [z[1] for z in leer_temperaturas()]) / len(temp)}")

@medir_tiempo
@auditar_funcion
def lista_original():
    for x in leer_temperaturas():
        print(f"{x[0]}: {x[1]}")

def llamar_n(funcion, veces):
    for i in range(veces):
        funcion()
   

def main():
    lista_original()
    filtrado()
    transformar()
    ordenar()
    reducir()
    llamar_n(reducir, 3)

main()
