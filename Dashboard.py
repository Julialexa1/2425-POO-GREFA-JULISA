import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Especifica la codificación UTF-8 para evitar errores de decodificación
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'Unidad 1/2.1. Programacion tradicional frente a POO/2.1-1 Tarea Programacion Tradicional.py',
        '3': 'Unidad 1/2.1. Programacion tradicional frente a POO/2.1-2 Tarea Programacion POO.py',
        '4': 'Unidad 1/EjemploMundoReal_POO semana 4/tarea sem. 4 ejemplo sistema de reservas.py',
        '5': 'Unidad 2 Elemntos de programacion/Tipos de datos, Identificadores/tarea semana 5 calcular area de una figura.py',
        '6': 'Unidad 2 Elemntos de programacion/Aplicación de Conceptos de POO en Python/Tarea semana 6 Programa de gestión de vehículos para una concesionaria.py',
        '7': 'Unidad 2 Elemntos de programacion/Constructores y destructores/tarea semana 7 Implementación de Constructores y Destructores.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()