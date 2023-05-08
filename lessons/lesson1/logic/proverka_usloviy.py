a = 1
b = 2

print('\n исходные данные переменных \n a = 1 \n b = 2 \n')

# вывод результатов проверки первой переменной
print('\nVariable a Is :' 'One' if (a == 1) else 'Not One')
print('\nVariable a Is :' 'Even' if (a % 2 == 0) else 'Odd')

# Результаты проверки второй переменной
print('\nVariable b Is :', 'One' if (b == 1) else 'Not One')
print('\nVariable b Is :', 'Even' if (b % 2 == 0) else 'Odd')

max = a if (a > b) else b
print('\nGreater  Value Is:', max)
