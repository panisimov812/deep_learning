title = '\n Python In Easy Steps\n'

for char in title: print(char, end=' ')
for char in title:
    print('*', end=' ')
    continue
    print(char, end=' ')

for char in title:
    if char == 'y':
        print('*', end=' ')
        continue
        print(char, end=' ')
