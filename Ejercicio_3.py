# Declarar vector con 7 notas
notas = []
suma = 0
# Ingresar notas
for i in range(7):
    nota = float(input("Ingrese la nota " + str(suma + 1) + ": "))
    notas.append(nota)

# Calcular resultados
nota_mayor = max(notas)
nota_menor = min(notas)
promedio = sum(notas) / len(notas)

# Mostrar resultados
print("La nota mayor es:", nota_mayor)
print("La nota menor es:", nota_menor)
print("Promedio:", promedio)
