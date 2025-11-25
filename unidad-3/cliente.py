#Se importa la clase Usuario del modulo usuario
from usuario import Usuario

#Se define la clase Cliente como subclase de Usuario
class Cliente(Usuario):
    """
    Representa un usuario cliente.

    Attributes:
        nombre (String): El nombre del usuario.
        correo (String): El correo electrónico del usuario.
        saldo (Float): El saldo del usuario.
    
    Methods:
        mostrar_info(): Metodo para entregar un resumen de la informacion del usuario.
    """
    #Se inicializa el constructor de la clase
    def __init__(self, nombre: str, correo: str, saldo: float):
        """
        Parameters:
            nombre (String): El nombre del usuario.
            correo (String): El correo electrónico del usuario.
            saldo (Float): El saldo del usuario.
        """
        #Se instancia el constructor de la clase padre
        super().__init__(nombre, correo) #HERENCIA DE CLASE USUARIO
        #Se inicializa el saldo
        self.saldo = saldo

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
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Saldo ${self.saldo:.2f}"
