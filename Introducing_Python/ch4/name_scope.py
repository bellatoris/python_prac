animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)

print_global()

def change_and_print_global():
    #print('insed change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)

change_and_print_global()

def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

change_local()
print(id(animal))

animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

print(animal)
change_and_print_global()
print(animal)

# locals() 함수는 로컬 네임스페이스의 내용이 담긴 딕셔너리를 반환
# globals() 함수는 글로벌 네임스페이스의 내용이 담긴 딕셔너리를 반환

animal = 'fruitbat'
def change_local():
    animal = 'wombat' # 지역변수
    print('locals:', locals())

print(animal)
change_local()
print('globals:', globals())
print(animal)

def amazing():
    '''This is the amazing function.
    Want to see it again?'''
    print('This function is named:', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)
    
amazing()
