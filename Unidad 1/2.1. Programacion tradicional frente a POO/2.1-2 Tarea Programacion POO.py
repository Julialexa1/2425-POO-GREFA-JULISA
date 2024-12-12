#POO
# Calcular promedio de temperatura semanal
#Crea una clase ClimaSemanal que encapsula los datos y las operaciones relacionadas

class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []  # Atributo para almacenar temperaturas

    # Método para ingresar temperaturas
    def ingresar_temperaturas(self):
        print("Ingresa la temperatura diaria de la semana (7 días):")
        for i in range(7):
            temp = float(input(f"Día {i + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if not self.temperaturas:
            print("No se han ingresado temperaturas.")
            return None
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
def main():
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    if promedio is not None:
        print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Llamar al programa principal
main()
