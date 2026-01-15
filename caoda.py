def procesar_datos(datos):
    resultado = 0
    resultado = 0  # variable duplicada (code smell)

    if datos is None:
        return None
    else:
        if len(datos) == 0:
            return None
        else:
            if len(datos) > 0:
                for i in range(len(datos)):
                    if datos[i] > 0:
                        if datos[i] % 2 == 0:
                            resultado = resultado + datos[i]
                        else:
                            if datos[i] % 3 == 0:
                                resultado = resultado + datos[i]
                            else:
                                if datos[i] % 5 == 0:
                                    resultado = resultado + datos[i]
                                else:
                                    resultado = resultado + 0
                    else:
                        if datos[i] == 0:
                            resultado = resultado + 0
                        else:
                            resultado = resultado - datos[i]

    return resultado


def imprimir(resultado):
    if resultado is not None:
        if resultado >= 0:
            if resultado >= 100:
                print("Resultado muy alto")
            else:
                if resultado >= 50:
                    print("Resultado medio")
                else:
                    if resultado >= 10:
                        print("Resultado bajo")
                    else:
                        print("Resultado muy bajo")
        else:
            print("Resultado negativo")
    else:
        print("Sin resultado")


def main():
    datos = [10, -3, 0, 7, 15, 22, 9, 30]
    r = procesar_datos(datos)
    imprimir(r)


if __name__ == "__main__":
    main()
