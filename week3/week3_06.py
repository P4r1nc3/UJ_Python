width = int(input("Enter width: "))
height = int(input("Enter height: "))
result = ""

for i in range (0, height):
	result = result +  "+---" * width + "+\n"
	result = result + "|   " * width + "|\n"

result = result + "+---" * width + "+\n"
print(result)