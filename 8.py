def main(palabra):
    cantidad_letras = dict()
    for letra in range(97, 123):
        if chr(letra) in palabra:
            cantidad_letras[chr(letra)] = palabra.count(chr(letra))
    return cantidad_letras


if __name__ == "__main__":
    print(main("Hola Mundo"))
