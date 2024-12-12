#Programacion Tradicional
# Calcular promedio de temperatura semanal
#Utiliza funciones independientes para manejar tareas específicas como la entrada de datos y el cálculo del promedio.

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingresa la temperatura diaria de la semana (7 días):")
    for i in range(7):
        temp = float(input(f"Día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Llamar al programa principal
main()
