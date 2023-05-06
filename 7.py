def is_valid_walk(walk):
    contador_x = 0
    contador_y = 0

    if len(walk) > 9:
        for direction in walk:
            if direction == 's':
                contador_y = contador_y - 1
            if direction == 'n':
                contador_y = contador_y + 1
            if direction == 'w':
                contador_x = contador_x - 1
            if direction == 'e':
                contador_x = contador_x + 1
        if contador_y + contador_x == 0:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    print(is_valid_walk(['n', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w']))