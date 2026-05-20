# Se crea una lista para almacenar cinco edades
edades = []

# Se solicita ingresar las 5 edades
for i in range (5):
    edad = int(input(f"Ingrese las edades {i + 1}: "))
edades.append(edad)

# Mostrar las edades mayores a 18
print("\nEdades mayores o iguales a 18 años:")
for edad in edades:
    if edad >= 18:
        print(edad)