# 4.1
guess_me = 7

def up_down(value, guess_me):
    if value < guess_me:
        return 'too low'
    elif value == guess_me:
        return 'just right'
    else: 
        return 'too high'
'''
while True:
    result = up_down(int(input()), guess_me)
    print(result)
    if result == 'just right':
        break;
'''

# 4.2
guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break;
    else:
        print('oops')
        break;
    start += 1

# 4.3
l = [3, 2, 1, 0]

for num in l:
    print(num)

# 4.4
l = [i for i in range(10) if i % 2 == 0]
print(l)

# 4.5
squares = {i: i ** 2 for i in range(10)}
print(squares)

# 4.6
odd = {i for i in range(10) if i % 2 != 0}
print(odd)

# 4.7
got = (char for char in 'Got ')
rng = (num for num in range(10))

for char in got:
    print(char)

for num in rng:
    print(num)

# 4.8
def harry_potter():
    return ['Harry', 'Ron' 'Hermione']

# 4.9
def odds():
    for i in range(10):
        if i % 2 == 1:
            yield i

for count, number in enumerate(odds(), 3):
    if count == 3:
        print(number)
        break;

# 4.10
def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

@test
def hi():
    pass

new_hi = test(hi)
new_hi()

# 4.11
class OopsException(Exception):
    pass

try:
    raise OopsException()
except OopsException as exc:
    print('Caught an oops')

# 4.12
titles = ['Create of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']

a = {}

for title, plot in zip(titles, plots):
    a[title] = plot

print(a)
