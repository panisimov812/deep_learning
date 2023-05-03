# вычесления вероятности победы исходя из среднего числа игр (number_of_toes)
weight = 0.1


def neural_network(input, weight):
    # умножение входного значения на весовой коэффицент
    prediction = input * weight
    return prediction


# среднее число игр
number_of_toes = [8.5, 9.5, 10, 9]
input = number_of_toes[0]
pred = neural_network(input, weight)
print(pred)
