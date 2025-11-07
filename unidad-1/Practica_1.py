#Se importan liberias
import time
import functools

def random_temp():
  return time.time_ns()%99

def leer_temperaturas():
  ciudades = [('Estado de México', 50), ('Nuevo León', 71), ('Tamaulipas', 77), ('Coahuila', 79), ('Jalisco', 81), ('Veracruz', 84), ('Guanajuato', 85), ('Sonora', 87), ('Baja California', 88), ('Chiapas', 90), ('Colima', 92), ('Michoacán', 93), ('Morelos', 95), ('Quintana Roo', 96), ('Sinaloa', 97), ('Baja California Sur', 0), ('Campeche', 1), ('Chihuahua', 4), ('Durango', 6), ('Guerrero', 7), ('Puebla', 9), ('Querétaro', 11), ('San Luis Potosí', 12), ('Aguascalientes', 13), ('Hidalgo', 14), ('Mexico City', 17), ('Nayarit', 19), ('Oaxaca', 20), ('Tabasco', 21), ('Yucatán', 22), ('Zacatecas', 24), ('Tlaxcala', 25)]
  for x in ciudades:
    yield x

def filtrado():
  return list(filter(lambda x: x[1] >= 30, leer_temperaturas()))

def transformar():
  return list(map(lambda x: f"Alerta de calor en {x[0]}: {x[1]}°C", leer_temperaturas()))

def ordenar():
  return sorted(leer_temperaturas(), key=lambda x: x[1], reverse = True)

def reducir():
  return functools.reduce(lambda x, y:  x + y, temp := [z[1] for z in leer_temperaturas()]) / len(temp)

def auditar_funcion(funcion):
  def wrapper():
    dic[funcion.__name__] += 1
    inicio = time.time()
    funcion()
    fin = time.time()
    print(f"Time: {fin - inicio:.4f} segundos")

    return wrapper
  

print(reducir.__name__)
