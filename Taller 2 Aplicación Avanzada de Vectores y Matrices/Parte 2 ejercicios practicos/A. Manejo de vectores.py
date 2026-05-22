# Cargar, modificar y analizar un vector

# Pedimos ingresar los valores al usuario
Vector = []
print("Ingresa 15 números enteros:")
for i in range(15):
    while True:
        try:
            valor = int(input(f"Ingresa valor {i+1}: "))
            Vector.append(valor)
            break
        except ValueError:
            print("Ingresa un número válido")
print("Vector original:", Vector)

# Mayor y menor valor junto a su posición y promedio
mayor = max(Vector)
pos_mayor = Vector.index(mayor)
menor = min(Vector)
pos_menor = Vector.index(menor)
promedio = sum(Vector) / len(Vector)

print(f"El mayor valor es {mayor} y se encuentra en la posición {pos_mayor}.")
print(f"El menor valor es {menor} y se encuentra en la posición {pos_menor}.")
print(f"El promedio de los valores es: {promedio:.2f}")

# Modificar valor
pos_modificar = int(input("Ingrese la posición que desea modificar (0 a 14): "))

if 0 <= pos_modificar <= 14:
    nuevo_valor = int(input("Ingrese el nuevo valor entero: "))
    Vector[pos_modificar] = nuevo_valor
    
    # Mostrar el vector actualizado
    print("\n--- Vector Actualizado ---")
    print(Vector)
else:
    print("Error: La posición ingresada está fuera del rango (0-14).")