def validar_subcuadricula_sudoku(matriz):
    # Convertir la matriz de 3x3 en una lista simple de 9 elementos
    numeros_ingresados = [num for fila in matriz for num in fila]
    
    # Conjunto con los números ideales de un sudoku
    valores_correctos = set(range(1, 10))
    
    # Identificar números repetidos y faltantes
    repetidos = set([x for x in numeros_ingresados if numeros_ingresados.count(x) > 1])
    faltantes = valores_correctos - set(numeros_ingresados)
    
    # Evaluar si la cuadrícula es válida
    if len(repetidos) == 0 and len(faltantes) == 0:
        print("✅ La cuadrícula de Sudoku es VÁLIDA.")
        return True
    else:
        print("❌ La cuadrícula de Sudoku NO es válida.")
        if repetidos:
            print(f"   -> Números repetidos: {list(repetidos)}")
        if faltantes:
            print(f"   -> Números faltantes: {list(faltantes)}")
        return False

# --- Ejemplos de prueba ---

# 1. Matriz Válida
matriz_valida = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Prueba 1:")
validar_subcuadricula_sudoku(matriz_valida)

print("\nPrueba 2:")
# 2. Matriz Inválida (Falta el 9, se repite el 5 y tiene un número fuera de rango)
matriz_invalida = [
    [1, 5, 3],
    [4, 5, 6],
    [7, 8, 10]
]

