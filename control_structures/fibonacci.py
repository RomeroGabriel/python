def fibonacci(amout):
    result = [0, 1]
    for _ in range(2, amout):
        result.append(sum(result[-2:]))
    return result


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
