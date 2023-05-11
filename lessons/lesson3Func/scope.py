global_var = 1


def my_vars():
    print('Globals Variable:', global_var)


local_var = 2
print('Local VariabeL', local_var)

global inner_var
inner_var = 3

my_vars()
print('Coerced Global: ', inner_var)
