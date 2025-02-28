#Sistema Avanzado de Gestión de Inventario
import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        """Convierte el objeto Producto a un diccionario para almacenamiento en JSON."""
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde un archivo JSON."""
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                return {int(k): Producto(**v) for k, v in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def guardar_inventario(self):
        """Guarda los productos en un archivo JSON."""
        with open(self.archivo, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.productos.items()}, f, indent=4)

    def agregar_producto(self, id, nombre, cantidad, precio):
        """Añade un nuevo producto al inventario."""
        if id in self.productos:
            print("Error: El ID ya existe.")
            return
        self.productos[id] = Producto(id, nombre, cantidad, precio)
        self.guardar_inventario()
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id):
        """Elimina un producto por ID."""
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print("Producto eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto por ID."""
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            self.guardar_inventario()
            print("Producto actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre."""
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(f"ID: {p.id}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
        else:
            print("No se encontraron productos.")

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            for p in self.productos.values():
                print(f"ID: {p.id}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
        else:
            print("Inventario vacío.")

# Menú interactivo
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(id, nombre, cantidad, precio)

        elif opcion == "2":
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
