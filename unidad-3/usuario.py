#Se importan librerias de abstraccion
from abc import ABC, abstractmethod

#Se define la clase abstracta Usuario como subclase de ABC
class Usuario(ABC): #ABSTRACCION
    """
    Representa un usuario en abstracto

    Attributes:
        nombre (String): El nombre del usuario.
        correo (String): El correo electrónico del usuario.
    
    Methods:
        mostrar_info(): Metodo abstracto de la clase, debe entregar un string.
    """
    #Se inicializa el constructor de la clase
    def __init__(self, nombre: str, correo: str):
        """
        Parameters:
            nombre (String): El nombre del usuario.
            correo (String): El correo del usuario.
        """
        #Se inicializa el nombre
        self.nombre = nombre
        #Se inicializa el correo
        self.correo = correo
    
    #Metodo abstracto para mostrar informacion decorada como metodo abstracto
    @abstractmethod  #DECORADOR
    def mostrar_info(self) -> str:
        """
        Metodo abstracto de mostrar informacion.
        
        Parameters:
            (None): No recibe nada.
        
        Returns:
            (String): Retorna una cadena.
        """
        #Se define de manera abstracta
        pass
