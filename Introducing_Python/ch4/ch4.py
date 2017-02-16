def document_it(func):
	def new_function(*args, **kwargs):
		print('Running function:', func.__name__)
		print('Positional arguments:', args)
		print('Keyword arguments:', kwargs)
		result = func(*args, **kwargs)
		print('Result:', result)
		return result
	return new_function

@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

animal = 'fruitbat'

def change_and_print_global():
	print('inside change_and_print_global:', animal)
	print('after the change:', animal)

change_and_print_global()

def change_and_print_global():
	global animal
	animal = 'wombat'
	print('inside change_and_print_global:', animal)

print(animal)
change_and_print_global()
print(animal)
