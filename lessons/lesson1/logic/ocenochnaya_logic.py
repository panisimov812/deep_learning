'''
    Оператор    |   Операция
       and      |     Логическое И   - вернет True если оба операнда имеют значение True в противном случае False
       or       |     Логическое ИЛИ - вернет True если хотябы один операнд имеет значение true
       not      |     Логическое НЕ  - возвращает противоположное значение от того который имеет опернад
'''

a = True
b = False

print('\n исходные данные переменных \n a = True \n b = False \n')

print('AND logic')
print('a AND a=', a and a)
print('a AND b=', a and b)
print('b AND b=', b and b)

print('\nOR Logic')
print('a or a', a or a)
print('a or b', a or b)
print('b or b', b or b)

print('\nNOT Logic')
print('a=', a, '\tnot a=', not a)
print('a=', b, '\tnot b=', not b)

'''
AND logic
a AND a= True
a AND b= False
b AND b= False

OR Logic
a or a True
a or b True
b or b False

NOT Logic
a= True 	not a= False
a= False 	not b= True
'''
