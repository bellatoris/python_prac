def do_nothing():
    pass

def make_a_sound():
    print('quack')


make_a_sound()

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))

print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

# 기본 인자값은 함수가 실행될 때 계산되지 않고, 함수를 정의할 때 계산된다.

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')
buggy('b')

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

nonbuggy('a')
nonbuggy('b')

nonbuggy('a', ['a'])

def print_args(*args):
    print('Positional argument tuple:', args)

print_args('a', 'b', 'c')

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Nedd this one too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle')

def print_kwargs(**kwargs):
    print('Keyword arguemtns:', kwargs)


print_kwargs(wine='merlot', entree='mutton')

def echo(anything):
    'echo returns its input argument'
    return anything

def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is ture.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)

#help(echo)
print(print_if_true.__doc__)


# In Python, function is first class
def answer():
    print(42)

answer()

def run_something(func):
    func()

run_something(answer)

print(type(run_something))

def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)

# *args는 함수가 임의의 갯수의 positional argument를 받을 수 있게 한다.
# 함수에서 받은 *args를 print(args) 할 경우 args는tuple임을 알 수 있고,
# print(*args) 할 경우 여러개의 인자로 표현된다.
# 그러므로 일반적인 함수의 경우 def func(arg1, arg2) 이렇게 정의되어 있으므로
# 그 함수에 다시 args를 넣을때는 func(*args)를 해야 여러개의 인자를 한번에 넣는것이다.

# 여기서는 sum이 하나의 tuple을 받는 함수 이므로 sum(args)로 넣어줘야한다.
def sum_args(*args):
    print(sum(args))

def run_with_positional_args(func, *args):
    print('args:', args)
    print('*args:', *args)
    return func(*args)

run_with_positional_args(sum_args, 1, 2, 3, 4)


def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(3, 4))

def knights(saying):
    def inner(quote):
        return "we are the knights who say: '%s'" % quote
    return inner(saying)
print(knights('Ni!'))

# Closure
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(type(a))
print(type(b))
print(a)
print(b)

print(a())
print(b())

# Lambda
def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']
def enliven(word):
    return word.capitalize() + '!'

edit_story(stairs, enliven)

edit_story(stairs, lambda x: x.capitalize() + '!')

print(list(map(lambda x: x ** 2, range(5))))

