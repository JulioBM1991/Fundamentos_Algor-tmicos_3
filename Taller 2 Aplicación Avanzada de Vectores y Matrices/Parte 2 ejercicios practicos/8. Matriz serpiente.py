def matriz_serpiente():
    # 1. Solicitar y validar el número N
    while True:
        try:
            n = int(input("Ingrese un número N (N >= 6): "))
            if n >= 6:
                break
            print("Error: El número debe ser mayor o igual a 6.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

    # 2. Crear la matriz vacía
    matriz = [[0] * n for _ in range(n)]
    
    # 3. Llenar la matriz con la lógica de serpiente
    contador = 1
    for i in range(n):
        # Si la fila es par, va de izquierda a derecha
        if i % 2 == 0:
            for j in range(n):
                matriz[i][j] = contador
                contador += 1
        # Si la fila es impar, va de derecha a izquierda
        else:
            for j in range(n - 1, -1, -1):
                matriz[i][j] = contador
                contador += 1

    # 4. Determinar el ancho máximo para la alineación limpia
    # (N*N determinará cuántos dígitos tiene el número más grande)
    ancho_maximo = len(str(n * n))

    # 5. Mostrar la matriz perfectamente alineada
    print("\nMatriz Serpiente Resultante:")
    for fila in matriz:
        # Explicación de f"{num:>{ancho_maximo}}": 
        # Alinea el número a la derecha con espacios según el tamaño del número más grande
        fila_formateada = " ".join(f"{num:>{ancho_maximo}}" for num in fila)
        print(fila_formateada)

# Ejecutar la función
matriz_serpiente()
