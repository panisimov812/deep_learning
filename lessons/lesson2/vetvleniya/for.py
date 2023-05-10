chars = ['A', 'B', 'C']
fruit = ('Apple', 'Banana', 'Cherry')
dict = {'name': 'Mike',
        'ref': 'Python',
        'sys': 'Win'}

print('\nElements:\t', end='')

# Инструкция для выводв всех элеентов
for item in chars:
    print(item, end=' ')

# Инструкция для вывода значения всех элементов списка а также индексов
print('\nEnumerated:\t', end=' ')
for item in enumerate(chars):
    print(item, end=' ')

# Инструкция вывода всех элементов списка и кортежа
print('\nZipped:\t', end=' ')
for item in zip(chars, fruit):
    print(item, end=' ')

# Инструкция вывода всех имен ключей словаря и связанных значений элементов
print('\nPaired:')
for key, value in dict.items():
    print(key, '=', value)
