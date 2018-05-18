def fibonacci(number):
    fib0 = 0
    fib1 = 1
    yield fib1
    for i in range(number - 1):
        fib = fib0 + fib1
        yield fib
        fib0 = fib1
        fib1 = fib
