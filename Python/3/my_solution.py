#ordenar numeros de mayor a menor


def descending_order(num):
    lista_de_numeros = list()
    for numero in str(num):
        lista_de_numeros.append(numero)

    lista_de_numeros.sort(reverse=True)
    return int("".join(lista_de_numeros))

if __name__ == "__main__":
    num = '987654321'
    print(descending_order(num))