# Clase para representar una Habitación
class Habitacion:
    def __init__(self, numero, tipo, precio):
        """
        Inicializa una habitación con número, tipo y precio.
        :param numero: Número de la habitación.
        :param tipo: Tipo de habitación (e.g., Individual, Doble).
        :param precio: Precio por noche.
        """
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservada = False  # Estado inicial: no reservada

    def reservar(self):
        """Marca la habitación como reservada."""
        if not self.reservada:
            self.reservada = True
            print(f"Habitación {self.numero} reservada exitosamente.")
        else:
            print(f"Habitación {self.numero} ya está reservada.")

    def cancelar_reserva(self):
        """Marca la habitación como no reservada."""
        if self.reservada:
            self.reservada = False
            print(f"Reserva de la habitación {self.numero} cancelada.")
        else:
            print(f"Habitación {self.numero} no está reservada.")

    def __str__(self):
        """Devuelve una representación en texto de la habitación."""
        estado = "Reservada" if self.reservada else "Disponible"
        return f"Habitación {self.numero}: Tipo {self.tipo}, Precio ${self.precio} ({estado})"


# Clase para gestionar el hotel y las habitaciones
class Hotel:
    def __init__(self, nombre):
        """
        Inicializa el hotel con un nombre y una lista de habitaciones.
        :param nombre: Nombre del hotel.
        """
        self.nombre = nombre
        self.habitaciones = []  # Lista de habitaciones del hotel

    def agregar_habitacion(self, habitacion):
        """
        Agrega una nueva habitación al hotel.
        :param habitacion: Objeto de la clase Habitacion.
        """
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        """Muestra todas las habitaciones del hotel con su estado."""
        print(f"\nHabitaciones del Hotel {self.nombre}:")
        for habitacion in self.habitaciones:
            print(habitacion)

    def buscar_habitacion_disponible(self, tipo):
        """
        Busca una habitación disponible por tipo.
        :param tipo: Tipo de habitación buscada.
        :return: Habitación disponible o None si no hay.
        """
        for habitacion in self.habitaciones:
            if habitacion.tipo == tipo and not habitacion.reservada:
                return habitacion
        return None


# Ejemplo de uso del sistema de reservas
if __name__ == "__main__":
    # Crear un hotel
    mi_hotel = Hotel("Paraiso")

    # Agregar habitaciones al hotel
    mi_hotel.agregar_habitacion(Habitacion(101, "Individual", 50))
    mi_hotel.agregar_habitacion(Habitacion(102, "Doble", 75))
    mi_hotel.agregar_habitacion(Habitacion(103, "Suite", 150))

    # Mostrar las habitaciones iniciales
    mi_hotel.mostrar_habitaciones()

    # Buscar y reservar una habitación de tipo Doble
    habitacion_disponible = mi_hotel.buscar_habitacion_disponible("Doble")
    if habitacion_disponible:
        habitacion_disponible.reservar()
    else:
        print("No hay habitaciones disponibles de este tipo.")

    # Intentar reservar una habitación ya reservada
    habitacion_disponible.reservar()

    # Cancelar la reserva
    habitacion_disponible.cancelar_reserva()

    # Mostrar el estado actualizado de las habitaciones
    mi_hotel.mostrar_habitaciones()
