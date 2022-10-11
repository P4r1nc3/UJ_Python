L = [1, 2, 3, 4, 5, 11, 22, 33, 44, 55, 111, 222, 333, 444, 555]

L2 = ' '.join(str(i).zfill(3) for i in L)
print(L2)