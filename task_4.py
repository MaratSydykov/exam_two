import numbers

def func(*args):
    sum = 0
    for i in args:
        if isinstance(i, numbers.Number):
            sum = sum + i
    return sum

print(func(5, 1, 7))
print(func(1, 'two', 3, 'four', 5))
input_data = [(5, 3, 1), 5.7, 'thirteen', 10, {1: 10}]
print(func(*input_data))