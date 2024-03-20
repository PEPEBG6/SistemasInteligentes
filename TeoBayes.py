def main():
    num_eventos = int(input("Ingrese el número de eventos: "))
    valores_A = []
    valores_B = []

    for i in range(num_eventos):
        A = float(input(f"Ingrese el valor de A{i+1}: "))
        B = float(input(f"Ingrese el valor de B{i+1}: "))
        valores_A.append(A)
        valores_B.append(B)

    evento = int(input("Ingrese el número del evento que desea calcular: "))
    probabilidad = calcular_probabilidad(valores_A, valores_B, evento)
    probabilidad_porcentaje = probabilidad * 100
    print("La probabilidad es:", f"{probabilidad_porcentaje:.2f}%")

def calcular_probabilidad(valores_A, valores_B, evento):
    sumatoria = sum(B * A for A, B in zip(valores_A, valores_B))
    probabilidad = (valores_B[evento - 1] * valores_A[evento - 1]) / sumatoria
    return probabilidad

if __name__ == "__main__":
    main()