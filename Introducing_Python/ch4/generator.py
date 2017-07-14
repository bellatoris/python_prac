def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number 
        number += step

print(my_range())

for num in my_range():
    print(num)
