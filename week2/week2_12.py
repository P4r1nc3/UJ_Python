line = 'dog cat \n frog         hamster\npig'
list = line.split()
#print(list)

first_letters = ""

for word in list:
	first_letters += word[0]
print(first_letters)

last_letters = ""

for word in list:
	last_letters += word[-1:]
print(last_letters)