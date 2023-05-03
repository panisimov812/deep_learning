# прогноз на победу или поражение или травм игрока

weights = [0.3, 0.2, 0.9]


def neural_network(input, weight):
    pred = ele_mul(input, weight)
    return pred


def ele_mul(number, vector):
    output = [0, 0, 0]
    assert (len(output) == len(vector))

    for i in range(len(vector)):
        output[i] = number * vector[i]
    return output


# передача одной точки данных
wlrec = [0.65, 0.8, 0.8, 0.9]
input = wlrec[0]
pred = neural_network(input, weights)
print(pred)

#Вход   вес     Итоговые прогнозы
#0.65 * 0.3   =   0.195 = Прогноз вероятности травмы
#0.65 * 0.2   =   0.13  = Прогноз вероятности победы
#0.65 * 0.9   =   0.585  = Прогноз вероятности огорчения
