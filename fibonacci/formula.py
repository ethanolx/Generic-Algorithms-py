def fib(n: int):
    return round((((1 + 5 ** 0.5) / 2) ** n) / (5 ** 0.5))

fib_string = '''
def fib(n: int):
    return round((((1 + 5 ** 0.5) / 2) ** n) / (5 ** 0.5))
'''

if __name__ == '__main__':
    print([fib(n) for n in range(1, 11)])