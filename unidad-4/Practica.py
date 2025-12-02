#Se importa libreria de testeo
import unittest

#Clase para generar las pruebas unitarias
class TestStringMethods(unittest.TestCase):
    #Prueba de entradas erroneas
    def test_total_bad(self):
        self.assertEqual(validar_datos("","", ""), 3)
    #Prueba de entradas correctas
    def test_total_good(self):
        self.assertEqual(validar_datos("Pepe", 25, "pepe@gmail.com"), 0)
    #Prueba de tipo diferente esperado en numero
    def test_not_type_number(self):
        self.assertEqual(validar_datos("Pepe", "25", "pepe@gmail.com"), 1)
    #Prueba de tipo diferente esperado en nombre
    def test_not_type_name(self):
        self.assertEqual(validar_datos(10, 25, "pepe@gmail.com"), 1)
    #Prueba de tipo diferente esperado en correo
    def test_not_type_email(self):
        self.assertEqual(validar_datos("Pepe", 25, [1,2]), 1)
    #Prueba de correo con formato incorrecto
    def test_wrong_email(self):
        self.assertEqual(validar_datos("Pepe", 25, "pepe@.com"), 1)
    #Prueba de edad en numero flotante
    def test_not_integer_number(self):
        self.assertEqual(validar_datos("Pepe", 1.1, "pepe@gmail.com"), 1)
        
#Funcion de validacion del problema
def validar_datos(nombre, edad, correo):
    """
    Funcion que realiza la validacion de tres campos en consola.

    Parameters:
        nombre (Any): El nombre del registro.
        edad (Any): La edad del registro.
        correo (Any): El correo del registro.
    
    Returns:
        errores (Integer): La cantidad de campos con error.
    """
    #Funcion de mensajes de inicio
    mensaje_inicio = lambda x: print(f"Iniciando validación del campo [{x}]:")
    #Funcion de mensajes de finales
    mensaje = lambda x, y: print(f"[{x}]: Validación completa. Cantidad de errores: {y}\n")
    #Funcion de mensajes de fallo
    mensaje_fallo = lambda x, y: print(f"ERROR: El atributo [{x}] {y}.\nRegistro finalziado.")
    #Contador de errores
    errores = 0
    #Se manda un mensaje de para mostrar el inicio de la valicacion del campo
    mensaje_inicio("nombre")
    try:
        #Se valida que no sea un texto vacío
        if nombre.replace(" ", "") == "":
            #Se genera un mensaje y se cuenta un error
            mensaje_fallo("nombre", "está vacío")
            errores += 1
        else:
            #Se remplazan espacios vacios
            nombre = nombre.replace(" ","").lower()
    except AttributeError:
        #Si hay un error de atributo y se cuenta error
        mensaje_fallo("nombre", "no es texto")
        errores += 1
    finally:
        #Mensaje de conclusion
        mensaje("nombre", errores)
    #Se manda un mensaje de para mostrar el inicio de la valicacion del campo
    mensaje_inicio("edad")
    try:
        #Si el tipo es flotante se manda error de valor
        if type(edad) == float:
            raise ValueError
        #Si es un entero menor a cero
        elif edad <= 0:
            #Se manda mensaje y se cuenta un error
            mensaje_fallo("edad", "es menor o igual a cero")
            errores += 1
    #Error de tipo
    except TypeError:
        #Se manda mensaje y se cuenta el error
        mensaje_fallo("edad", "no es un número")
        errores += 1
    #Error de valor
    except ValueError:
        #Se manda mensaje y se cuenta el error
        mensaje_fallo("edad", "no es entero")
        errores += 1
    finally:
        #Mensaje de finalizacion
        mensaje("edad", errores)
    #Se manda un mensaje de para mostrar el inicio de la valicacion del campo
    mensaje_inicio("correo")
    try:
        #Se intenta obtener el formato entre el arroba
        if len(partes := correo.split("@")) != 2 or (len(partes[0]) == 0 or len(partes[1]) == 0):
            #Si no es un formato coherente se manda mensaje y se cuenta el error
            mensaje_fallo("correo", "no tiene un formato adecuado")
            errores += 1
        #Se realzia una separacion en la seccion derecha del arroba
        elif len(dominio := partes[1].split(".")) == 2:
            #Si las partes son vacias se manda un error de indice
            if (len(dominio[0]) == 0 or len(dominio[1]) == 0):
                raise IndexError
        else:
            #En caso contrario se manda error de indice
            raise IndexError
    #Error de valor
    except ValueError:
        #Se manda mensaje y cuenta un error
        mensaje_fallo("correo", "no es texto")
        errores += 1
    #Error de indice
    except IndexError:
        #Se manda mensaje y cuenta un error
        mensaje_fallo("correo", "no posee un dominio correcto")
        errores += 1
    #Error de atributo
    except AttributeError:
        #Se manda mensaje y cuenta un error
        mensaje_fallo("correo", "no es un correo")
        errores += 1
    finally:
        #Se manda mensaje de finalizacion
        mensaje("correo", errores)
    #Se retorna la cantidad de errores
    return errores

#Funcion de llamada a los test unitarios
def probar_validaciones():
    """
    Funcion que ejecuta los test unitarios.

    Parameters:
        (None): No recibe nada.
    
    Returns:
        (None): No retorna nada.
    """
    #Se ejecutan las pruebas
    unittest.main()

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

#Funcion de validacion de tipo para las entradas de consola
def val_input(campo: str):
    """
    Funcion que valida si un campo es de un tipo de dato numerico o no, y entrega su conversion.

    Parameters:
        campo (String): El campo a validar.
    
    Returns:
        campo (String): Si no es numerico.
        (Integer): Si es entero.
        (Float): Si es flotante.
    """
    #Se intenta validar que sea un entero
    try:
        #Si se puede generar la conversión es un entero
        if float(campo) == int(campo):
            #Se regresa el entero
            return int(campo)
    except ValueError:
        #Se intenta reccuperar el flotante
        try:
            #Se retorna el flotante
            return float(campo)
        except:
            #Se retorna el campo original
            return campo
    except:
        #Se retorna el campo original ante excepciones extra
        return campo

#Funcion de arranque
if __name__ == "__main__":
    #Se manda un mensaje de entrada
    print("Bienvenido")
    #Bucle para pedir datos
    while True:
        #Se muestra un menu de seleccion
        print("¿Desea registrar un usuario? Presione una tecla...\n[S]: Para iniciar un registro.\n[Cualquier otra tecla]: Para salir.")
        #Se valida la tecla de escape
        if input().lower() != "s":
            #Escape
            break 
        #Se llama a la validacion y se piden campos
        validar_datos(
            #Se pide el campo nombre sin validacion
            pedir_campo("nombre", lambda x: True), 
            #Se pide el campo edad simulando una adaptacion de tipo
            val_input(pedir_campo("edad", val_input)), 
            #Se pide el campo correo sin validacion
            pedir_campo("correo", lambda x: True)
            )
    #Mensaje de separador
    print("--------> PRUEBAS UNITARIAS...\n")
    #Se ejecutan las pruebas unitarias
    probar_validaciones()
