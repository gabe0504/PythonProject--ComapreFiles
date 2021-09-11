d={'Canada': 'ca', 'United States':'us', 'Mexico':'mx'}
if 'Canada' in d:
    print('a. Canada in dict\n' + 'True\n')
else:
    print('a. Canada in dict\n' + 'False\n')
if 'France' in d:
    print('b. France in dict\n' + 'True\n')
else:
    print('b. France in dict\n' + 'False\n')
print('c. Keys and values in dict (key in field width 20)')
for x in d:
    print(format(x, '20'), d.get(x))
d['Sweden']='sw'
print('\nd. Dict with Sweden set to \'sw\':')
print(d)
del d['Sweden']
d['Sweden']='se'
print('\ne. Dict with Sweden set to \'se\':')
print(d)
d2 = {abbr: name for name, abbr in d.items()}
print("\nf. Reverse mapping using dictionary comprehension:")
print(d2)
print('\ng. Reverse mapping uppercase using dictionary comprehension: ')
d2 = {abbr: name.upper() for name, abbr in d.items()}
print(d2)
