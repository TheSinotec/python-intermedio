def validar_datos(nombre, edad = "", correo = ""):
    try:
        if nombre.replace(" ", "") == "":
            print("El atributo [nombre] está vacío.")
    except AttributeError:
        print("El atributo [nombre] no es texto.")
    finally:
        print("Se ha validado el atributo [nombre].\n")


    try:
        if type(edad) == float:
            raise ValueError
        elif edad <= 0:
            print("El atributo [edad] es menor o igual a cero.")
    except TypeError:
        print("El atributo [edad] no es un número.")
    except ValueError:
        print("El atributo [edad] no es entero.")
    finally:
        print("Se ha validado el atributo [edad].\n")
    

    try:
        if len(partes := correo.split("@")) != 2 or (len(partes[0]) == 0 or len(partes[1]) == 0):
            print("El atributo [correo] no tiene un formato adecuado. Verifique cerca del '@'")
        elif len(dominio := partes[1].split(".")) <= 1:
            if (len(dominio[0]) == 0 and len(dominio[1]) == 0):
                raise IndexError
    except ValueError:
        print("El atributo [correo] no es texto.")
    except IndexError:
        print("El atributo [correo] no posee un dominio correcto.")
    finally:
        print("Se ha validado el atributo [correo].\n")

if __name__ == "__main__":
    validar_datos("a", 1, "a@.a")
