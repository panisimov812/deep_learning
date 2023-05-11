def echo(user, lang, sys):
    print('User:', user, 'Language:', lang, 'Platforma:', sys)


echo('Petr', 'Python', 'Windows')


def mirror(user='Mike', lang='Python'):
    print('\nUser:', user, 'Language:', lang)


mirror()
mirror(lang='Java')
mirror(user='Tony')
mirror('Susan','C++')