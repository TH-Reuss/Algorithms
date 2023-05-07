def get_middle(s):
    return s[:int(len(s)/2)][-1:] + s[int(len(s)/2):][:1] if len(s) % 2 == 0 else s[int(len(s)/2)]
        

if __name__ == "__main__":
    print(get_middle("A"))