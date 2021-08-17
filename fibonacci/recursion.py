def fib(n: int):
    if n >= 2:
        return fib(n - 1) + fib(n - 2)
    else:
        return n

print([fib(n) for n in range(1, 11)])

fib_string = '''
def fib(n: int):
    if n >= 2:
        return fib(n - 1) + fib(n - 2)
    else:
        return n
'''