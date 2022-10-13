string1 = "Ring-a-Ring o’Roses"
string2 = "Hickory Dickory Dock"

common_list = []
for item in string1:
    if item in string2 and item not in common_list:
        common_list.append(item)
        
print(common_list)
final_list = list(set(string1+string2))
print(final_list)