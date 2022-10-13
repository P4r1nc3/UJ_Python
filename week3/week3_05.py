length = int(input("Enter a length of the ruler: "))
ruler = ("|...")
print(ruler*length + "|")

for i in range(0, length+1):
    if i < 9:
        print(i, end = '')
        print("   ", end = '')
    else:
        print(i, end = '')
        print("  ", end = '')