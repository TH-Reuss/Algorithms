def maskify(cc):
    if len(cc) > 4:
        numeros_ocultos = "#" * (len(cc) - 4)
        maskify_text = numeros_ocultos + cc[-4:]
        return maskify_text
    else:
        return cc


if __name__ == "__main__":
    texto_prueba = "Nananananananananananananananana Batman!"
    print(maskify(texto_prueba))