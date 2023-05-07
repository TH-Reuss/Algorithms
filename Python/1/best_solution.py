def to_camel_case(text):
    removed = text.replace("_", " ")
    removed = text.replace("-", " ")
    text = removed.split(" ")

    new_text = list()

    for index, word in enumerate(text):
        if index == 0:
            new_text.append(word)
        else:
            new_text.append(word.title())

    return "".join(new_text)


if __name__ == "__main__":
    print(to_camel_case("the-stealth-warrior"))
