"""
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
# ^ w python nie konczymy linii srednikami

for i in "axby": if ord(i) < 100: print (i)
# ^ nieprawidlowe formatowanie kodu, ktore w pythonie jest bardzo istotne

for i in "axby": print (ord(i) if ord(i) < 100 else i)
# ^ nieprawidlowe formatowanie kodu, ktore w pythonie jest bardzo istotne

"""