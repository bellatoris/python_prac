years_list = [1980, 1981, 1982, 1983, 1984]
years_list[2]
years_list[-1]
things = ['mozzarella', 'cinderella', 'salmonella']
print(things[0].title())
print(things)

f2e = {
    'dog': 'chien', 
    'cat': 'chat',
    'walrus': 'morse'
    }

print(f2e)
print(f2e['walrus'])
e2f = {}
for key, value in f2e.items():
    e2f[value] = key

print(e2f)
print(e2f.keys())

life = {
    'animals': {
	'cats': 'Henri',
	'octopi': 'Grumpy',
	'emus': 'Lucy'
    },
    'plants': {},
    'other': {}
}

print(life)

print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])

