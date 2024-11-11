def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        return f'{str(a)}{str(b)}'
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))



