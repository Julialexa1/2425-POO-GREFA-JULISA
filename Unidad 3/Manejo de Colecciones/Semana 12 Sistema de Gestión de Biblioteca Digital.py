# Sistema de Gestion de Biblioteca Digital

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla para título y autor (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} - {self.info[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id  # ID único
        self.prestamos = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros con ISBN como clave
        self.usuarios = set()  # Conjunto de IDs de usuarios
        self.prestamos = {}  # Diccionario de préstamos {user_id: [lista de libros]}

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya existe en la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios:
            self.usuarios.add(usuario.user_id)
            self.prestamos[usuario.user_id] = []
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            if not self.prestamos[user_id]:  # No debe tener libros prestados
                self.usuarios.remove(user_id)
                del self.prestamos[user_id]
                print(f"Usuario con ID {user_id} eliminado.")
            else:
                print("El usuario tiene libros prestados. No se puede eliminar.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            if isbn not in [libro.isbn for libro in self.prestamos[user_id]]:
                self.prestamos[user_id].append(self.libros[isbn])
                print(f"Libro prestado: {self.libros[isbn]} a Usuario ID {user_id}")
            else:
                print("El usuario ya tiene este libro prestado.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in [libro.isbn for libro in self.prestamos[user_id]]:
            self.prestamos[user_id] = [libro for libro in self.prestamos[user_id] if libro.isbn != isbn]
            print(f"Libro con ISBN {isbn} devuelto por Usuario ID {user_id}")
        else:
            print("Libro no encontrado en los préstamos del usuario.")

    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros.values() if valor.lower() in getattr(libro, criterio).lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros.")

    def listar_prestamos_usuario(self, user_id):
        if user_id in self.prestamos and self.prestamos[user_id]:
            print(f"Libros prestados a Usuario ID {user_id}:")
            for libro in self.prestamos[user_id]:
                print(libro)
        else:
            print("No hay libros prestados para este usuario.")


# Ejemplo de uso
def main():
    biblioteca = Biblioteca()

    libro1 = Libro("El principito", "Antoine de Saint-Exupéry", "Ficción", "12345")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "67890")

    usuario1 = Usuario("Julisa", 1)
    usuario2 = Usuario("Miguel", 2)

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    biblioteca.prestar_libro(1, "12345")
    biblioteca.listar_prestamos_usuario(1)

    biblioteca.devolver_libro(1, "12345")
    biblioteca.listar_prestamos_usuario(1)

    biblioteca.buscar_libro("categoria", "Novela")


if __name__ == "__main__":
    main()
