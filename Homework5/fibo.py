def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = result
        return result

    return fibonacci

fib = caching_fibonacci()

print(fib(100))
print(fib(9))
print(fib(8))
print(fib(7))
print(fib(10))



