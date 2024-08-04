import random
from collections import Counter

# Problema 1: Matriz de enteros
def cuenta_numeros(matriz):
    todos_los_numeros = [num for fila in matriz for num in fila]
    conteo = Counter(todos_los_numeros)
    unicos = sum(1 for num, cnt in conteo.items() if cnt == 1)
    repetidos = sum(1 for num, cnt in conteo.items() if cnt > 1)
    
    return [unicos, repetidos]

def generar_matriz(n, rango):
    return [[random.randint(1, rango) for _ in range(n)] for _ in range(n)]

# Problema 2: Pares de numeros
def pares_suma_n(n):
    pares = []

    for i in range(1, n // 2 + 1):
        pares.append((i, n - i))
    
    return pares

def generar_numero(max_valor):
    return random.randint(1, max_valor)

def main():
    n_matriz = 3
    rango_matriz = 10
    max_n = 1000000  #n (10^6)
    max_pares_mostrar = 10

    matriz = generar_matriz(n_matriz, rango_matriz)
    print("Matriz generada:")
    for fila in matriz:
        print(fila)
    
    resultado_matriz = cuenta_numeros(matriz)
    print(f"\nResultado de cuenta_numeros: {resultado_matriz}")

    n = generar_numero(max_n)
    print(f"\nNumero generado: {n}")

    resultado_pares = pares_suma_n(n)
    
    print(f"\nPares que suman {n} (mostrando los primeros {max_pares_mostrar} pares):")
    for i, par in enumerate(resultado_pares[:max_pares_mostrar]):
        print(par)
    
    if len(resultado_pares) > max_pares_mostrar:
        print(f"... y {len(resultado_pares) - max_pares_mostrar} pares mas.")
    
    numeros_sumados = list(set(num for par in resultado_pares for num in par))
    print(f"\nNumeros utilizados para formar los pares: {numeros_sumados}")


if __name__ == "__main__":
    main()
