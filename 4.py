def open_or_senior(data):
    output = list()

    for age , score in data:
        #age = member[0]
        #score = member[1]

        if age > 54 and score > 7:
            output.append("Senior")
        else:
            output.append("Open")
    
    return output

if "__main__" == __name__:
    data =  [(45, 12),(55,21),(19, -2),(104, 20)]
    print(open_or_senior(data))