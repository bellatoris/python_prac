def document_it(func):
    '''
    new_function은func에 필요한 args와 kwargs를 한곳에 모으고 
    그 것을 다시 풀어서 func(*args, **kwargs)로 집어넣는다.
    '''
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)


@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 4)

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints(a, b):
    return a + b

add_ints(3, 4)
