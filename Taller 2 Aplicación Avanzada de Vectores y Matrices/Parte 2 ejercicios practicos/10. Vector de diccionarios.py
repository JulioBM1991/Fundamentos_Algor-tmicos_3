import random

# Generar el vector de diccionarios de forma aleatoria
def generar_estudiantes(cantidad=8):
    nombres = ["Ana", "Juan", "Luis", "María", "Pedro", "Elena", "Carlos", "Sofía", "Diego", "Laura"]
    estudiantes = []
    
    for _ in range(cantidad):
        estudiante = {
            "nombre": random.choice(nombres),
            "edad": random.randint(15, 25),
            "nota": round(random.uniform(1.0, 5.0), 1)
        }
        estudiantes.append(estudiante)
    return estudiantes

# Filtrar estudiantes mayores de 18 años
def filtrar_mayores_de_18(estudiantes):
    return [e for e in estudiantes if e["edad"] > 18]

# Listar estudiantes que aprobaron (nota >= 3.0)
def listar_aprobados(estudiantes):
    return [e for e in estudiantes if e["nota"] >= 3.0]

# Obtener el nombre o nombres con la nota más alta
def obtener_mejor_nota(estudiantes):
    if not estudiantes:
        return []
    
    # Encontrar la nota máxima
    max_nota = max(e["nota"] for e in estudiantes)
    
    # Filtrar todos los que tengan esa nota máxima (por si hay empates)
    mejores = [e["nombre"] for e in estudiantes if e["nota"] == max_nota]
    return mejores, max_nota

# --- PRUEBA DEL PROGRAMA ---
# 1. Crear la lista
lista_estudiantes = generar_estudiantes(8)
print("--- Lista Completa de Estudiantes ---")
for e in lista_estudiantes:
    print(e)

# 2. Aplicar filtros
print("\n--- Estudiantes Mayores de 18 Años ---")
print(filtrar_mayores_de_18(lista_estudiantes))

print("\n--- Estudiantes Aprobados (Nota >= 3.0) ---")
print(listar_aprobados(lista_estudiantes))

# 3. Obtener el mejor
mejores_nombres, nota_alta = obtener_mejor_nota(lista_estudiantes)
print(f"\n--- Mejor Nota ({nota_alta}) ---")
print(f"Estudiante(s): {', '.join(mejores_nombres)}")
