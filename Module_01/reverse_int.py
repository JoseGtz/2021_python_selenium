def reverse_int(number: int) -> int:
    aux = str(number)
    aux = aux[::-1]
    if isinstance(number, int):
        number = int(aux)
    else:
        number = float(aux)
    return number


x = 12345.234
print(reverse_int(x))