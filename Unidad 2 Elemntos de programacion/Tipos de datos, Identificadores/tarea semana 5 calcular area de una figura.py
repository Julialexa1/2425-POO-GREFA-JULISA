# Programa para calcular el área de un círculo

# Descripción: Este programa calcula el área de un círculo a partir de su radio.
# Utiliza la fórmula: Área = π * radio^2

import math  # Importamos el módulo math para utilizar el valor de pi

def calcular_area_circulo(radio):
  """Calcula el área de un círculo.

  Args:
    radio: El radio del círculo.

  Returns:
    El área del círculo.
  """

  area = math.pi * radio ** 2
  return area

# Pedimos al usuario que ingrese el radio
radio = float(input("Ingrese el radio del círculo: "))

# Calculamos el área utilizando la función
area_total = calcular_area_circulo(radio)

# Imprimimos el resultado
print("El área del círculo es:", area_total)