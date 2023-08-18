def make_ruler(length):
    ruler = ("|...")
    result1 = ruler*length + "|"
    result2 = ""

    for i in range(0, length+1):
        if i < 9:
            result2 += str(i) + "   "
        else:
            result2 += str(i) + "  "

    result_finall = result1 + "\n" + result2
    return result_finall

def make_grid(width, height):
    result = ""

    for i in range (0, height):
        result = result +  "+---" * width + "+\n"
        result = result + "|   " * width + "|\n"

    result = result + "+---" * width + "+\n"
    return result

if __name__ == "__main__":
    #RULER
    length = int(input("Enter a length of the ruler: "))
    print(make_ruler(length))

    #GRID
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    print(make_grid(width, height))