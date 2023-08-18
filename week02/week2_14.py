line = 'dog cat \n frog         hamster\npig'
list = line.split()

max_length = 0
longest = ""

for word in list:
    if max_length  < len(word):
        max_length  = len(word)
        longest= word

print(max_length)
print(longest)