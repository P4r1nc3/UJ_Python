def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

while(True):
	number = input("Enter a number: ")
    
	if isfloat(number):
		print("%s %s" % (float(number) , float(number) * float(number)))
	elif (number == "stop") :
		print("Bye! Bye!")
		break
	else :
		print("Something went wrong")		
		continue