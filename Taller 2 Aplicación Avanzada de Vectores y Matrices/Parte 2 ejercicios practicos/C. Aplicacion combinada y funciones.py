# Constante para los 6 meses de historial
MESES = 6

def cargar_datos():
    """Pide la cantidad de productos y llena el vector y la matriz."""
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos a registrar: "))
            if cantidad > 0:
                break
            print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

    nombres = []
    inventario = []

    for i in range(cantidad):
        nombre = input(f"\nIngrese el nombre del producto {i + 1}: ").strip()
        nombres.append(nombre)

        print(f"Ingrese el inventario de los últimos {MESES} meses para '{nombre}':")
        historial_producto = []
        
        j = 0
        while j < MESES:
            try:
                cantidad_mes = int(input(f"  Mes {j + 1}: "))
                if cantidad_mes < 0:
                    print("  La cantidad no puede ser negativa. Intente de nuevo.")
                    continue
                historial_producto.append(cantidad_mes)
                j += 1
            except ValueError:
                print("  Entrada inválida. Por favor, ingrese un número entero.")
        
        inventario.append(historial_producto)

    return nombres, inventario


def calcular_promedios_extremos(nombres, inventario):
    """Calcula y muestra el producto con mayor y menor inventario promedio."""
    max_promedio = -1.0
    min_promedio = float('inf')
    prod_max = ""
    prod_min = ""

    for i in range(len(nombres)):
        suma_producto = sum(inventario[i])
        promedio = suma_producto / MESES

        if promedio > max_promedio:
            max_promedio = promedio
            prod_max = nombres[i]
            
        if promedio < min_promedio:
            min_promedio = promedio
            prod_min = nombres[i]

    print(f"Producto con MAYOR inventario promedio: {prod_max} ({max_promedio:.2f} unidades/mes)")
    print(f"Producto con MENOR inventario promedio: {prod_min} ({min_promedio:.2f} unidades/mes)")


def mostrar_inventario_total(inventario):
    """Muestra la suma de todo el inventario de todos los productos y meses."""
    # Suma todos los elementos de la matriz bidimensional
    total_general = sum(sum(fila) for fila in inventario)
    print(f"Inventario total acumulado (todos los productos y meses): {total_general} unidades")


def consultar_producto(nombres, inventario):
    """Busca un producto por su nombre y calcula su inventario total."""
    busqueda = input("Ingrese el nombre del producto que desea consultar: ").strip()
    
    # Buscamos de forma insensible a mayúsculas/minúsculas para mayor comodidad
    nombres_minuscula = [n.lower() for n in nombres]
    
    if busqueda.lower() in nombres_minuscula:
        indice = nombres_minuscula.index(busqueda.lower())
        total_producto = sum(inventario[indice])
        print(f"El inventario total de '{nombres[indice]}' en los {MESES} meses es de: {total_producto} unidades.")
    else:
        print(f"El producto '{busqueda}' no se encuentra en el sistema.")


# --- Bloque Principal de Ejecución ---
if __name__ == "__main__":
    # 1. Carga y almacenamiento de datos
    vector_nombres, matriz_inventario = cargar_datos()
    
    # 2. Análisis del inventario
    print("\n--- ANÁLISIS DE INVENTARIO ---")
    calcular_promedios_extremos(vector_nombres, matriz_inventario)
    mostrar_inventario_total(matriz_inventario)
    
    # 3. Módulo de consulta
    print("\n--- CONSULTA DE PRODUCTO ---")
    consultar_producto(vector_nombres, matriz_inventario)
