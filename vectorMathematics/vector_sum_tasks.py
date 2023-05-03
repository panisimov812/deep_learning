weight = [0.1, 0.2, 0.3]

a = [0, 1, 0, 1]
b = [1, 0, 1, 0]
c = [0, 1, 1, 0]

def elementwise_addition(vec_a):
    assert (len(vec_a))
    output = 0

    for i in range(len(vec_a)):
        output += (vec_a[i])
    return output


def test_network(input, weight):
    prediction = elementwise_addition(input)
    return prediction


input = [a[0], b[0], c[0]]
pred = test_network(input, weight)
print(pred)
