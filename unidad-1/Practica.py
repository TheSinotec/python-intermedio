#Se importan liberias
import time
import functools

#Decorador para medir el tiempo de ejecucion de una funcion
def medir_tiempo(funcion):
    """
    Decorador para computar el tiempo de ejecucion de una llamada a funcion.
    """
    def wrapper():
        #Se registra el tiempo de inicio
        inicio = time.time()
        #Se ejecuta la funcion
        funcion()
        #Se registra el tiempo de fin de la funcion
        fin = time.time()
        #Se imprime la diferencia entre tiempos
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos.\n")
    return wrapper

#Decorador para mostrar el nombre de funcion y contar la cantidad de llamadas
def auditar_funcion(funcion):
    """
    Decorador para mostrar el nombre de la funcion ejecutada y contar las veces que se hace.
    """
    #Se inicializa un diccionario como contador de las llamadas de las funciones
    dic = {"filtrado": 0, "transformar": 0, "ordenar": 0, "reducir": 0, "lista_original": 0}
    def wrapper():
        #Se cuenta la llamada a la funcion
        dic[funcion.__name__] += 1
        #Se imprime el nombre de la funcion
        print(f"\nLa función '{funcion.__name__}' se está ejecutando...")
        #Se ejecuta la funcion
        funcion()
        #Se muestra un mensaje con la cantidad de llamadas realizadas
        print(f"Se ha ejecutado {dic[funcion.__name__]} ve{"z" if dic[funcion.__name__] == 1 else "ces"}.")
    return wrapper

#Generador de las tuplas (<ciudad>, <temperatura>)
def leer_temperaturas():
    """
    Generador de una lista de tuplas de la forma (<ciudad>, <temperatura>).

    Parameters:
        None: No recibe nada.
    
    Returns:
        None: No retorna nada.
    """
    #Se simulan los registros mediante una lista
    ciudades = [('Estado de México', 50), ('Nuevo León', 71), ('Tamaulipas', 77), ('Coahuila', 79), ('Jalisco', 81), ('Veracruz', 84), ('Guanajuato', 85), ('Sonora', 87), ('Baja California', 88), ('Chiapas', 90), ('Colima', 92), ('Michoacán', 93), ('Morelos', 95), ('Quintana Roo', 96), ('Sinaloa', 97), ('Baja California Sur', 0), ('Campeche', 1), ('Chihuahua', 4), ('Durango', 6), ('Guerrero', 7), ('Puebla', 9), ('Querétaro', 11), ('San Luis Potosí', 12), ('Aguascalientes', 13), ('Hidalgo', 14), ('Mexico City', 17), ('Nayarit', 19), ('Oaxaca', 20), ('Tabasco', 21), ('Yucatán', 22), ('Zacatecas', 24), ('Tlaxcala', 25)]
    #Ciclo para servir cada tupla
    for x in ciudades:
        #Se sirve cada tupla
        yield x

#Se colocan ambos decoradores para medir tiempo y auditar
@medir_tiempo
@auditar_funcion
#Funcion que imprime una lista de temperaturas mayores o igual a 30
def filtrado():
    """
    Imprime una lista de temperaturas mayor o igual a 30, de a cuerdo al generador leer_temperaturas.

    Parameters:
        None: No recibe nada.
    
    Returns:
        None: No retorna nada.
    """
    #Ciclo que recorre la lista filtrada del generador e imprime sus valores
    for x in list(filter(lambda x: x[1] >= 30, leer_temperaturas())):
        #Se da formato a la impresion de los datos
        print(f"{x[0]}: {x[1]}")

#Se colocan ambos decoradores para medir tiempo y auditar
@medir_tiempo
@auditar_funcion
#Funcion que imprime una lista de temperaturas formateadas en un texto de alerta
def transformar():
    """
    Imprime una lista de temperaturas en formato de texto segun el generador leer_temperaturas.

    Parameters:
        None: No recibe nada.
    
    Returns:
        None: No retorna nada.
    """
    #Ciclo que recorre la lista formateada del generador e imprime sus valores
    for x in list(map(lambda x: f"Alerta de calor en {x[0]}: {x[1]}°C", leer_temperaturas())):
        #Se imprimen los datos
        print(x)

#Se colocan ambos decoradores para medir tiempo y auditar
@medir_tiempo
@auditar_funcion
#Funcion que imprime y ordena una lista de temperaturas en orden descendente de su temperatura
def ordenar():
    """
    Imprime una lista de temperaturas ordenadas en orden descendente segun el generador leer_temperaturas.

    Parameters:
        None: No recibe nada.
    
    Returns:
        None: No retorna nada.
    """
    #Ciclo que recorre la lista ordenada por temperatura del generador e imprime sus valores
    for x in sorted(leer_temperaturas(), key=lambda x: x[1], reverse = True):
        #Se da formato a la impresion de los datos
        print(f"{x[0]}: {x[1]}")

#Se colocan ambos decoradores para medir tiempo y auditar
@medir_tiempo
@auditar_funcion
#Funcion que imprime el promedio de temperaturas en un formato requerido
def reducir():
    """
    Imprime un mensaje y el promedio de las temperaturas segun el generador leer_temperaturas.

    Parameters:
        None: No recibe nada.
    
    Returns:
        None: No retorna nada.
    """
    #Se imprime el promedio de las temperaturas en un mensaje
    print(f"Temperatura promedio de alertas: {functools.reduce(lambda x, y:  x + y, temp := [z[1] for z in leer_temperaturas()]) / len(temp)}")

#Se colocan ambos decoradores para medir tiempo y auditar
@medir_tiempo
@auditar_funcion
#Funcion que imprime la lista original del generador
def lista_original():
    """
    Imprime una lista de temperaturas completa segun el generador leer_temperaturas.

    Parameters:
        None: No recibe nada.
    
    Returns:
        None: No retorna nada.
    """
    #Ciclo que imprime la lista del generador
    for x in leer_temperaturas():
        #Se da formato a la impresion de los datos
        print(f"{x[0]}: {x[1]}")

#Funcion para realizar una cantidad fija de llamadas de una funcion
def llamar_n(funcion, veces):
    """
    Realiza una cantidad determinada de llamadas a una funcion.

    Parameters:
        None: No recibe nada.
    
    Returns:
        None: No retorna nada.
    """
    #Ciclo para realizar una cantidad fija de llamadas a una funcion
    for i in range(veces):
        #Se invoca la funcion
        funcion()
   
#Funcion de arranque
def main():
    """
    Funcion de arranque, para inicializar el sistema.

    Parameters:
        None: No recibe nada.
    
    Returns:
        None: No retorna nada.
    """
    #Se imprime la lista original
    lista_original()
    #Se imprime el filtrado de los datos
    filtrado()
    #Se imprime la lista transformada como texto
    transformar()
    #Se imprime la lista reordenada descendente por temperaturas
    ordenar()
    #Se imprime el promedio de las temperaturas
    reducir()
    #Se llama 3 veces a la funcion reducir para corroborar la cantidad de llamadas
    llamar_n(reducir, 3)

#Se corre el sistema
main()
