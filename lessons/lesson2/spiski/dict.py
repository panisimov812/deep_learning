dict = {'name': 'bob',
        'ref': 'Python',
        'sys': 'Win'}


print('Dictionary', dict)
print('\nReference (Еденичное значенеи по ключу)', dict['ref'])

print('\nKeys (Все ключи, содержащиеся в словаре', dict.keys())

del dict['name']
dict['user'] = 'Tom'
print('/nDictionary', dict)

#поиск по ключу
print('name' in dict)