# Programa para demostrar el uso de constructores y destructores en Python
# Este programa simula un sistema básico de gestión de usuarios.

class User:
    """
    Clase que representa a un usuario en el sistema.
    Utiliza constructor para inicializar atributos y destructor para limpiar recursos.
    """

    def __init__(self, username, email):
        """
        Metodo Constructor que inicializa los atributos del objeto.

        :param username: Nombre del usuario
        :param email: Correo electrónico del usuario
        """
        self.username = username
        self.email = email
        print(f"Usuario '{self.username}' creado con éxito.")

    def display_info(self):
        """
        Muestra la información del usuario.
        """
        print(f"Nombre de usuario: {self.username}")
        print(f"Correo electrónico: {self.email}")
# Metodo destructor
    def __del__(self):
        """
        Destructor que se activa cuando el objeto es eliminado.
        Limpia recursos asociados con el objeto (si aplica).
        """
        print(f"El usuario '{self.username}' ha sido eliminado del sistema.")


# Demostración del uso de constructores y destructores
def main():
    print("=== Sistema de Gestión de Usuarios ===")

    # Creación de objetos (se llama al constructor __init__)
    user1 = User("Luis", "luis1@gmail.com")
    user2 = User("Juan", "juan2@gmail.com")

    # Uso de métodos de la clase
    print("\nInformación del Usuario 1:")
    user1.display_info()

    print("\nInformación del Usuario 2:")
    user2.display_info()

    # Eliminación de un objeto (se llama al destructor __del__)
    print("\nEliminando usuario 1...")
    del user1

    print("Eliminando usuario 2...")
    del user2

    print("\n=== Fin del programa ===")


# Ejecución del programa principal
if __name__ == "__main__":
    main()
