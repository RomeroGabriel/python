def fibonacci(amout, values=(0, 1)):
    if len(values) == amout:
        return values
    return fibonacci(amout, values + (sum(values[-2:]), ))


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
