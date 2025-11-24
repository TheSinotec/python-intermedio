#Se importa la clase Producto del modulo producto
from producto import Producto
#Se importa la clase Cliente del modulo cliente
from cliente import Cliente

#Se define la clase Venta
class Venta:
    """
    Representa una venta a un Cliente de diversos Productos

    Attributes:
        cliente (Cliente): El cliente como objeto Cliente
        productos (list<Producto>): La lista de productos comprados como lista de objetos Producto.
    
    Methods:
        agregar_producto(producto): Agrega un objeto Producto a la lista de productos de la venta.
        total(): Regresa la suma de todos los precios generados en la venta.
    """
    #Se llama al constructor de la clase
    def __init__(self, cliente: Cliente): #AGREGACION
        #Se inicializa el cliente
        self.cliente = cliente
        #Se inicializa una lista
        self.productos: list[Producto] = []
    
    #Funcion para agregar un producto a la lista de productos
    def agregar_producto(self, producto: Producto) -> None:
        #Se agrega el producto a la lista
        self.productos.append(producto)

    #Funcion para entregar el total de los precios de la lista de productos
    def total(self) -> float:
        #Se regresa el total de la lista segun sus precios
        return sum(p.precio for p in self.productos)
