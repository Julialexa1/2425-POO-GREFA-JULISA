# Programa de gestión de vehículos para una concesionaria.
# Este programa utiliza los principios de POO, incluyendo herencia, encapsulación y polimorfismo.

class Vehiculo:
    """
    Clase base que representa un vehículo genérico.
    """
    def __init__(self, marca: str, modelo: str, precio: float):
        self.__marca = marca  # Atributo privado (encapsulación)
        self.__modelo = modelo  # Atributo privado (encapsulación)
        self.precio = precio  # Atributo público

    # Métodos para acceder a los atributos encapsulados
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def set_precio(self, nuevo_precio: float):
        if nuevo_precio > 0:
            self.precio = nuevo_precio
        else:
            print("El precio debe ser un valor positivo.")

    def mostrar_informacion(self):
        """
        Muestra la información básica del vehículo.
        """
        return f"Vehículo: {self.__marca} {self.__modelo}, Precio: ${self.precio:.2f}"

#Subclase
class Automovil(Vehiculo):
    """
    Clase derivada que representa un automóvil.
    """
    def __init__(self, marca: str, modelo: str, precio: float, tipo_motor: str):
        super().__init__(marca, modelo, precio)  # Llamada al constructor de la super clase
        self.tipo_motor = tipo_motor  # Atributo específico de la clase derivada

    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase base (polimorfismo).
        """
        return f"Automóvil: {self.get_marca()} {self.get_modelo()}, Motor: {self.tipo_motor}, Precio: ${self.precio:.2f}"

#Subclase
class Motocicleta(Vehiculo):
    """
    Clase derivada que representa una motocicleta.
    """
    def __init__(self, marca: str, modelo: str, precio: float, cilindrada: int):
        super().__init__(marca, modelo, precio)  # Llamada al constructor de la clase base
        self.cilindrada = cilindrada  # Atributo específico de la clase derivada

    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase base (polimorfismo).
        """
        return f"Motocicleta: {self.get_marca()} {self.get_modelo()}, Cilindrada: {self.cilindrada}cc, Precio: ${self.precio:.2f}"


# Programa principal
if __name__ == "__main__":
    # Crear instancias de las clases
    vehiculo_generico = Vehiculo("Genérico", "ModeloX", 15000)
    automovil = Automovil("Toyota", "Corolla", 22000, "Híbrido")
    motocicleta = Motocicleta("Yamaha", "YZF-R3", 5300, 321)

    # Demostrar encapsulación
    print(vehiculo_generico.mostrar_informacion())
    vehiculo_generico.set_precio(16000)
    print("Nuevo precio:", vehiculo_generico.mostrar_informacion())

    # Demostrar herencia y polimorfismo
    print(automovil.mostrar_informacion())
    print(motocicleta.mostrar_informacion())
