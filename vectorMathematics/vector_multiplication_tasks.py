weight = [0.1, 0.2, 0.3]

a = [8.5, 9.5, 9.9, 9.0]
b = [8.3, 1.5, 2.9, 9.0]
c = [8.3, 1.5, 2.9, 9.0]


def elementwise_multiplication(vec_a, vec_b):
    assert (len(vec_a) == len(vec_b))
    output = 0

    for i in range(len(vec_a)):
        output += (vec_a[i] * vec_b[i])
    return output


def test_network(input, weight):
    prediction = elementwise_multiplication(input, weight)
    return prediction


input = [a[0], b[0], c[0]]
pred = test_network(input, weight)
print(pred)
