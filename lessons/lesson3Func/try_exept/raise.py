day = 32

try:
    if day > 31:
        raise ValueError('Invalide Day Number')
except ValueError as msg:
    print('The Program found An', msg)
finally:
    print('But today Is Beautiful Anyway')
