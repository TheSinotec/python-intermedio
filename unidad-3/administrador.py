#Se importa la clase Usuario del modulo usuario
from usuario import Usuario

#Se define la clase Administracion como subclase de Usuario
class Administrador(Usuario):
    """
    Representa un usuario administrador

    Attributes:
        nombre (String): El nombre del usuario.
        correo (String): El correo electrónico del usuario.
        permisos (list<String>): El conjunto de permisos.
    
    Methods:
        mostrar_info(): Metodo para entregar un resumen de la informacion del usuario.
    """
    #Se inicializa el constructor de la clase
    def __init__(self, nombre: str, correo: str, permisos: list[str]):
        """
        Parameters:
            nombre (String): El nombre del usuario.
            correo (String): El correo electrónico del usuario.
            permisos (list<String>): El conjunto de permisos.
        """
        #Se instancia el constructor de la clase padre
        super().__init__(nombre, correo)
        #Se inicializan los permisos
        self.permisos = permisos
    
    #Metodo para generar un resumen de la informacion del usuario
    def mostrar_info(self) -> str:
        """
        Metodo para mostrar un resumen de informacion.
        
        Parameters:
            (None): No recibe nada.
        
        Returns:
            (String): Retorna una cadena con un resumen de la informacion de usuario.
        """
        #Se retorna una cadena de resumen de la informacion
        return f"Administrador: {self.nombre}, Correo: {self.correo}, Permisos: {', '.join(self.permisos)}"
