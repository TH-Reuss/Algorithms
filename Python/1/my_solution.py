def to_camel_case(text):
    
    nueva_oracion = list()
    palabra = list()
    
    for letra in text:
        if letra == "-" or letra == "_":
            print("".join(palabra))
            nueva_oracion.append("".join(palabra))
            palabra.clear()
            
        else:
            palabra.append(letra)
    
    nueva_oracion.append("".join(palabra))

    for index, palabra in enumerate(nueva_oracion):
        if index == 0:
            pass
        else:
            nueva_oracion[index] = palabra.title()
    
    return "".join(nueva_oracion)


if __name__ == "__main__":
    print(to_camel_case("the-stealth-warrior"))
