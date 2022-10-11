line = 'dog cat \n frog         hamster\npig'
list = line.split()

length = sum(len(word) for word in list)

print(length)