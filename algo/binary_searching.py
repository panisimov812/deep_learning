# бинарный поиск обязательно должен проводиться в отсартированном масиве
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= item:           #пока эта часть не сократиться до одного элемента
        mid = (low + high) // 2  #Проверяем средний элемент
        guess = list[mid]        #присвоение в массив
        if guess == item:        #значение найдено
            return mid
        if guess > item:         # если много
            high = mid - 1
        else:                    # мало
            low = mid + 1
    return None                  #значение не существует


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 9))
