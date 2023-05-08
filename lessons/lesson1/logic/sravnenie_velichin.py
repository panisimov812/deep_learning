'''
    Оператор  | Проверяемое условие   | Возвращает
    ==        |  Равенство            | True - если значения ровны
    !=        |  Неравенство          | True - если оба операнда не равны
    >         |  Больше
    <         |  Меньше
    >=        |  Юольше либо равно
    <=        |  Меньше либо равно
'''

nil = 0
num = 0
max = 1
cap = "A"
low = 'a'

print('Equality: \t', nil, '==', num, nil == num)
print('Equality: \t', cap, '==', num, cap == num)
print('Inequality: \t', nil, '!=', max, nil != max)
print('Greater: \t', nil, '>', max, nil > max)
print('Lesser: \t', nil, '<', max, nil < max)
print('More or equal : \t', nil, '>=', num, nil >= max)
print('Less or Equal: \t', max, '<=', num, max < num)

'''
Equality: 	 0 == 0 True
Equality: 	 A == 0 False
Inequality: 	 0 != 1 True
Greater: 	 0 > 1 False
Lesser: 	 0 < 1 True
More or equal : 	 0 >= 0 False
Less or Equal: 	 1 <= 0 False
'''
