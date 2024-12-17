'''
A feladatokban nem használhat min, max, sum, count, sort, reverse függvényeket! A listákat nem másolhatja át másik segédlistába!
Készítsen programot, amely bekér egy városnevet és ha az szerepel a listában, akkor kiírja az azt követő város nevét! Ha a bekért város az utolsó város volt, akkor jelezze, hogy nincs következő! Amennyiben pedig nem szerepel a listában, akkor vegye fel a lista végére!
'''

varosok=["Debrecen", "Karcag", "Szolnok", "Szeged", "Miskolc"]
index = 0
varos = 0

while varos != "stop":
    varos = input("Írj be egy városnevet: ")
    
    for i in varosok:
        if i == varos:
            for varosindex in varosok:
                index += 1
                if varosindex == i:
                    print(varosok[index])
                    break

        if varos == varosok[-1]:
            print("Nincs következő")
            break

        if varos not in varosok:
            varosok.append(varos)
            break

    print(varosok)