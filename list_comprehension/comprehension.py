import sys
doubles = [i * 2 for i in range(10)]
print(doubles)

even_doubles = [i * 2 for i in range(1000) if i % 2 == 0]
# print(even_doubles)


# generator
# use less memory
# generate by demand
generator = (i * 2 for i in range(1000) if i % 2 == 0)
print(next(generator))  # 0
print(next(generator))  # 4
print(next(generator))  # 8
print(next(generator))  # 12
print(next(generator))  # 16
# print(next(generator)) Error

print('\nMemory used comparison:')
print(f'Size of list: {sys.getsizeof(even_doubles)}')
print(f'Size of generator: {sys.getsizeof(generator)}')


generator_2 = (i * 2 for i in range(10) if i % 2 == 0)
for number in generator_2:
    print(number)

dic = {f'Number {i}:': i * 2 for i in range(10) if i % 2 == 0}
print(dic)

for number, double in dic.items():
    print(f'{number} x 2: {double}')


def get_date_type(day):
    days = {
        (1, 7): 'weekend',
        tuple(range(1, 7)): 'week'
    }
    day_chosen = (_type for days, _type in days.items() if day in days)
    return next(day_chosen, '** invalid **')


for day in range(0, 9):
    print(f'Day: {day}: {get_date_type(day)}')
