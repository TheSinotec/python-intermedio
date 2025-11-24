from venta import Venta
from cliente import Cliente
from producto import Producto

class Tienda:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.ventas: dict[Venta] = {}
        self.clientes: dict[Cliente] = {}
        self.productos: dict[Producto] = {}

    def registrar_venta(self, cliente: Cliente, venta: list[Producto]) -> None:
        self.ventas[cliente] = Venta(cliente)
        for x in venta:
            self.ventas[cliente].agregar_producto(x)
        
    def registrar_producto(self, nombre: str, precio: float) -> None:
        self.productos[nombre] = Producto(nombre, precio) if nombre not in self.productos.keys() else print("El producto ya existe.")
        
    def registrar_cliente(self, nombre: str, correo: str, saldo: float) -> None:
        self.clientes[nombre] = Cliente(nombre, correo, saldo) if nombre not in self.clientes.keys() else print("El cliente ya existe.")

    def mostrar_resultado(self, nombre: str = ""):
        if nombre != "":
            print(self.clientes[nombre].mostrar_info())
            print(f"Total de la venta: ${self.ventas[nombre].total():.2f}") if nombre in self.ventas.keys() else print("Total de la venta: $0.00")
        print(f"\nVentas registradas en toda la tienda: {len(self.ventas.keys())}")
