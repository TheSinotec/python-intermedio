#Se define la clase Producto
class Producto:
    """
    Representa un Producto

    Attributes:
        contador_productos (Integer): Atributo de clase para contar los productos.
        nombre (String): Representa el nombre del producto.
        precio (Float): Respresenta el precio del producto.
    
    Methods:
        es_precio_valido(precio): Realiza una validacion respecto a un precio diferente de cero.
        total_productos(): Regresa el valor de la cantidad de los productos contados.
    """
    #Se inicialzia el atributo de clase contador_productos
    contador_productos = 0

    #Se inicializa el constructor de la clase
    def __init__(self, nombre: str, precio: float):
        """
        Parameters:
            contador_productos (Integer): Atributo de clase para contar los productos.
            nombre (String): Representa el nombre del producto.
            precio (Float): Respresenta el precio del producto.
        """
        #Se inicializa el nombre
        self.nombre = nombre
        #Se inicializa el precio
        self.precio = precio
        #Se actualiza el contador de clase
        Producto.contador_productos += 1

    #Metodo estatico para validacion de precio
    @staticmethod
    def es_precio_valido(precio: float) -> bool:
        """
        Metodo que valida si un precio es mayor a cero
        
        Parameters:
            precio (Float): El precio de un producto.
        
        Returns:
            Boolean == True: Si precio es un número flotante mayor a cero.
            Boolean == False: Si precio no es un número flotante mayor a cero.
        """
        #Regresa la validación de precio
        return precio > 0
    
    #Metodo para regresar el contador decorado como metodo de clase
    @classmethod
    def total_productos(cls) -> int:
        """
        Metodo que regresa el contador de productos
        
        Parameters:
            (None): No recibe nada.
        
        Returns:
            contador_productos (Integer): El contador de productos.
        """
        #Regresa el contador de la clase
        return cls.contador_productos
