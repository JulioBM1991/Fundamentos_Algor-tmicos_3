# 1. Solicitar dimensiones de la matriz
num_estudiantes = int(input("Ingrese el número de estudiantes: "))
num_notas = int(input("Ingrese la cantidad de notas por estudiante: "))

# Crear la matriz vacía
matriz_notas = []

# 2. Llenar la matriz con los datos del usuario
for i in range(num_estudiantes):
    print(f"\n--- Notas del Estudiante {i + 1} ---")
    notas_estudiante = []
    
    for j in range(num_notas):
        nota = float(input(f"Ingrese la nota {j + 1}: "))
        notas_estudiante.append(nota)
        
    matriz_notas.append(notas_estudiante)

# Variables para rastrear al mejor estudiante
mejor_promedio = -1.0
indice_mejor_estudiante = -1

# 3. Procesar y mostrar los resultados
print("\n=== RESUMEN DE NOTAS ===")
for i in range(num_estudiantes):
    notas = matriz_notas[i]
    promedio = sum(notas) / len(notas)
    
    # Mostrar información del estudiante actual
    print(f"Estudiante {i + 1}: Notas: {notas} | Promedio: {promedio:.2f}")
    
    # Verificar si es el mayor promedio encontrado
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        indice_mejor_estudiante = i

# 4. Mostrar al estudiante con el mayor promedio
print("\n=== MEJOR ESTUDIANTE ===")
print(f"El estudiante con mayor promedio es el Estudiante {indice_mejor_estudiante + 1}")
print(f"Índice / Fila de la matriz: {indice_mejor_estudiante}")
print(f"Promedio obtenido: {mejor_promedio:.2f}")