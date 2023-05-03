# веса
weight = [0.1, 0.2, 0]


# вычесление взвешанной суммы
def w_sum(a, b):
    assert (len(a) == len(b))
    output = 0

    for i in range(len(a)):
        # каждое входное значение умножается на весовой коэфицент а резльтат складывается
        output += (a[i] * b[i])
    #окончательый результат называется взвешанная сумма входов или скалярное произведение
    return output


def neural_network(input, weight):
    # умножение входного значения на весовой коэффицент
    prediction = w_sum(input, weight)
    return prediction


# текущее среднее число игр сыгранное игроками
toes = [8.5, 9.5, 9.9, 9.0]
# текущая доля игр, окончившихся победой (процент)
wlrec = [0.65, 0.8, 0.8, 0.9]
# число болельщиков
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wlrec[0], nfans[0]]
pred = neural_network(input, weight)
print(pred)
