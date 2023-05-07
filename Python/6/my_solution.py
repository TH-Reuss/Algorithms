def array_diff(a, b):
    for x in b:
        while x in a:
            a.remove(x)
    return a

if __name__ == "__main__":
    print(array_diff([1,2,2,2,3],[2]))   