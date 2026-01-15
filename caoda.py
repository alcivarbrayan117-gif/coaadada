def analizar_numeros(numeros):
    """
    Analiza una lista de números y devuelve estadísticas.
    """
    if numeros is None or len(numeros) == 0:
        raise ValueError("La lista no puede estar vacía")

    suma = 0
    maximo = numeros[0]
    minimo = numeros[0]
    pares = 0
    impares = 0

    for num in numeros:
        suma += num

        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num

        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

    promedio = suma / len(numeros)

    return {
        "suma": suma,
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo,
        "pares": pares,
        "impares": impares
    }


def imprimir_resultados(resultado):
    """
    Imprime los resultados del análisis.
    """
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")


def main():
    datos = [10, 3, 7, 8, 15, 22, 9]
    resultado = analizar_numeros(datos)
    imprimir_resultados(resultado)


if __name__ == "__main__":
    main()
