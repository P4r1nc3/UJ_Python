line = "car ball door window eyes nose elbow longest"

alphabetic_order = sorted(line.split())
print(alphabetic_order)

length_order = sorted(line.split(), key = len)
print(length_order)