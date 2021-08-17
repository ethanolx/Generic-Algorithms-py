def fib(n: int):
    return round((((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / (5 ** 0.5))

def fib_less(n: int):
    return round((((1 + 5 ** 0.5) / 2) ** n) / (5 ** 0.5))

print([fib(n) for n in range(1, 11)])

fib_string = '''
def fib(n: int):
    return round((((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / (5 ** 0.5))
'''

fib_less_string = '''
def fib(n: int):
    return round((((1 + 5 ** 0.5) / 2) ** n) / (5 ** 0.5))
'''