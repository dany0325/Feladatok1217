'''
A feladatokban nem használhat min, max, sum, count, sort, reverse függvényeket! A listákat nem másolhatja át másik segédlistába!
Töltsön fel egy listát 100db véletlen egész számmal -100 .. +100 tartományból!
a) Ezt követően határozza meg, hogy 0-tól nagyobb vagy kisebb számból van-e több!
b) Keresse meg az első 50-től nagyobb számot és írja ki a sorszámát! (0-tól indulót) Ha nincs ilyen, akkor pedig azt!
c) Van-e olyan eset, hogy két egymást követő szám közötti különbség meghaladja a 120-at?
'''

import random
lst = []

for i in range(0,100):
    lst.append(random.randint(-100,100))

pos_nums = 0
neg_nums = 0
index = 0
first_larg_than_50 = 0

for i in lst:
    if i > 0:
        pos_nums += 1
    elif i < 0:
        neg_nums += 1

    if i > 50:
        first_larg_than_50 = index
    

    index += 1
    
if neg_nums > pos_nums:
    print('Negatív számokból van több')
else:
    print('Positív számokból van több')
    
print("Az első 50-től nagyobb szám sorszáma: ", first_larg_than_50)