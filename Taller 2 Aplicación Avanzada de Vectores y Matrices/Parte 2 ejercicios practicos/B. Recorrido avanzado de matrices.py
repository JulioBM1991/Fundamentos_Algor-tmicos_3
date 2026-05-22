procesar_matriz():
    # 1. Solicitar el tamaño de la matriz cuadrada
    N = int(input("Ingrese el tamaño N de la matriz cuadrada: "))
    
    # 2. Llenar la matriz con datos del usuario
    matriz = []
    print(f"\nIngrese los elementos de la matriz {N}x{N}:")
    for i in range(N):
        fila = []
        for j in range(N):
            valor = float(input(f"Elemento [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    
    # Mostrar la matriz ingresada para verificación visual
    print("\n--- Matriz Ingresada ---")
    for fila in matriz:
        print(fila)
        
    # 3. Inicializar las variables para los cálculos
    suma_principal = 0
    suma_secundaria = 0
    elementos_encima = []
    
    # 4. Recorrer la matriz para extraer los datos solicitados
    for i in range(N):
        for j in range(N):
            # Condición para la diagonal principal
            if i == j:
                suma_principal += matriz[i][j]
                
            # Condición para la diagonal secundaria
            if i + j == N - 1:
                suma_secundaria += matriz[i][j]
                
            # Condición para los elementos por encima de la diagonal principal
            if j > i:
                elementos_encima.append(matriz[i][j])
                
    # 5. Imprimir los resultados finales
    print("\n--- Resultados ---")
    print(f"Suma de la diagonal principal: {suma_principal}")
    print(f"Suma de la diagonal secundaria: {suma_secundaria}")
    print(f"Elementos por encima de la diagonal principal: {elementos_encima}")