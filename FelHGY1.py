'''
A feladatokban nem használhat min, max, sum, count, sort, reverse függvényeket! A listákat nem másolhatja át másik segédlistába!
Készítsen programot, amely bekér 5 mondatot, majd kiírja a legtöbb szóközt tartalmazó mondatot!
'''

sentences = []
current_space_count = 0
old_space_count = 0
print_sent = ""

for i in range(0,5):
    sentences.append(input('Írj be egy mondatot: '))

for sentence in sentences:
    for char in sentence:
        if char == " ":
            current_space_count += 1
    if old_space_count < current_space_count:
        print_sent = sentence
    old_space_count = current_space_count

print(print_sent)