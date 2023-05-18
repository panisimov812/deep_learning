import sys, keyword
print('Python Version: ', sys.version)
#Расположение интерпретатора пайтон в ОС
print('Python Interpretator Location: ', sys.executable)

print('Python Moduls Search Path: ')
for dir in sys.path:
    print(dir)

#Инструкция для вывода ключевых слов
print('Python Keywords: ')
for word in keyword.kwlist:print(word)