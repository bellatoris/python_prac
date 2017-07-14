number_list = []
for number in range(1, 6):
    number_list.append(number)

print(number_list)
number_list = list(range(1, 6))
print(number_list)
number_list = [number-1 for number in range(1, 6)]
print(number_list)
a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)
a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)

print(a_list)

rows = range(1,4)
print(rows)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row, col)

cells = [(row, col) for row in rows for col in cols]
for cell in cells: 
    print(cell)

for row, col in cells:
    print(row, col)

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

number_thing = (number for number in range(1, 6))
for number in number_thing:
    print(number)

number_list = list(number_thing)
print(number_list)
