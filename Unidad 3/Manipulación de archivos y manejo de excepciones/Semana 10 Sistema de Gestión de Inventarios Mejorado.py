#Sistema de Gestión de Inventarios Mejorado
import os

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor de la clase Producto"""
        self.id_producto = id_producto  # Identificador único
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible
        self.precio = precio  # Precio unitario

    def __str__(self):
        """Representación en cadena del objeto Producto"""
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    def to_dict(self):
        """Convierte el objeto Producto en un diccionario"""
        return {"id": self.id_producto, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    @staticmethod
    def from_dict(data):
        """Crea un objeto Producto a partir de un diccionario"""
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])


# Clase Inventario
class Inventario:
    FILE_NAME = "inventario.txt"

    def __init__(self):
        """Constructor de la clase Inventario"""
        self.productos = []  # Lista para almacenar los productos
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        """Guarda los productos en un archivo de texto"""
        try:
            with open(self.FILE_NAME, "w") as file:
                for producto in self.productos:
                    file.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio}\n")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        """Carga los productos desde un archivo de texto"""
        if not os.path.exists(self.FILE_NAME):
            return
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    id_producto, nombre, cantidad, precio = line.strip().split(",")
                    self.productos.append(Producto(id_producto, nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            print("Archivo de inventario no encontrado, se creará uno nuevo.")
        except ValueError:
            print("Error en el formato del archivo de inventario.")

    def agregar_producto(self, producto):
        """Añadir un nuevo producto al inventario, asegurando un ID único"""
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: Ya existe un producto con este ID.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Eliminar un producto por su ID"""
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado, si existía en el inventario.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualizar la cantidad o el precio de un producto por su ID"""
        for p in self.productos:
            if p.id_producto == id_producto:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Buscar productos por nombre (puede haber nombres similares)"""
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return encontrados

    def mostrar_productos(self):
        """Mostrar todos los productos en el inventario"""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)


# Función para mostrar el menú interactivo
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventarios Mejorado ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no cambia): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre o parte del nombre a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


# Ejecutar el menú interactivo
if __name__ == "__main__":
    menu()
