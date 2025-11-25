#Se importa la clase Venta del modulo venta
from venta import Venta
#Se importa la clase Cliente del modulo cliente
from cliente import Cliente
#Se importa la clase Producto del modulo producto
from producto import Producto

from functools import reduce

#Se define la clase Tienda
class Tienda:
    """
    Representa una Tienda

    Attributes:
        nombre (String): Respresenta el nombre de la tienda.
        ventas (dict<Venta>): Representa un diccionario de ventas.
        clientes (dict<Cliente>): Representa un diccionario de clientes.
        productos (dict<Producto>): Representa un diccionario de productos.
    
    Methods:
        registrar_venta(cliente, venta): Registra todas las compras de una venta de un cliente.
        registrar_producto(nombre, precio): Registra un producto.
        registrar_cliente(nombre, correo, saldo): Registra un cliente.
        mostrar_resultado(nombre): Imprime la informacion de un cliente sobre sus compras y la tienda.
    """
    #Se inicializa el constructor de la clase
    def __init__(self, nombre: str):
        """
        Parameters:
            nombre (String): Respresenta el nombre de la tienda.
            ventas (dict<Venta>): Representa un diccionario de ventas.
            clientes (dict<Cliente>): Representa un diccionario de clientes.
            productos (dict<Producto>): Representa un diccionario de productos.
        """
        #Se inicializa el nombre
        self.nombre = nombre
        #Se inicializa un diccionario de ventas
        self.ventas: dict[Venta] = {}
        #Se inicializa un diccionario de clientes
        self.clientes: dict[Cliente] = {}
        #Se inicializa un diccionario de productos
        self.productos: dict[Producto] = {}

    #Metodo para registrar la venta de un cliente segun una lista de productos
    def registrar_venta(self, cliente: Cliente, venta: list[Producto]) -> None:
        """
        Metodo para registrar la venta de un cliente segun una lista de productos
        
        Parameters:
            cliente (Cliente): El cliente que genera la venta.
            venta (list<Producto>): Lista de productos que comprenden la venta.
        
        Returns:
            (None): No retorna.
        """
        costo = reduce(lambda x, y:  x + y, [z.precio for z in venta])
        if costo > self.clientes[cliente].saldo:
            print("\nNo se puede realizar la compra. Saldo insuficiente.")
        else:
            #Se crea la venta si no existe
            if cliente not in self.ventas.keys():
                #Se crea el objeto venta
                self.ventas[cliente] = Venta(cliente) #COMPOSICION
            #Se recorre la lista de productos comprados
            for x in venta:
                #Se agrega el producto a la venta
                self.ventas[cliente].agregar_producto(x)
            self.clientes[cliente].saldo -= costo
    
    #Metodo para registrar un nuevo producto
    def registrar_producto(self, nombre: str, precio: float) -> None:
        """
        Metodo para registrar un nuevo producto
        
        Parameters:
            nombre (String): El nombre del producto.
            precio (Float): El precio del producto.
        
        Returns:
            (None): No retorna.
        """
        #Se crea el producto si no existe, o manda mensaje en el caso contrario
        self.productos[nombre] = Producto(nombre, precio) if nombre not in self.productos.keys() else print("El producto ya existe.")
    
    #Metodo para registrar un nuevo cliente
    def registrar_cliente(self, nombre: str, correo: str, saldo: float) -> None:
        """
        Metodo para registrar un nuevo cliente
        
        Parameters:
            nombre (String): El nombre del cliente.
            correo (String): El correo del cliente.
            saldo (Float): El saldo del cliente.
        
        Returns:
            (None): No retorna.
        """
        #Se crea el cliente si no existe, o manda mensaje en el caso contrario
        self.clientes[nombre] = Cliente(nombre, correo, saldo) if nombre not in self.clientes.keys() else print("El cliente ya existe.")

    #Metodo para mostrar en pantalla la informacion de cliente y tienda
    def mostrar_resultado(self, nombre: str = ""):
        """
        Metodo para registrar un nuevo cliente
        
        Parameters:
            nombre (String): El nombre del cliente. Por defecto vacío.
        
        Returns:
            (None): No retorna.
        """
        #Se validan cadenas vacías
        if nombre != "":
            #Se muestra informacion del cliente
            print(self.clientes[nombre].mostrar_info())
            #Se muestra el total de venta del cliente
            print(f"Total de la venta: ${self.ventas[nombre].total():.2f}") if nombre in self.ventas.keys() else print("Total de la venta: $0.00")
        #Se muestar un resumen de las ventas de la tienda
        print(f"\nVentas registradas en toda la tienda: {len(self.ventas.keys())}")
