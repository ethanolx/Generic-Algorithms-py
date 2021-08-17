def fib(n: int):
    if n >= 2:
        return fib(n - 1) + fib(n - 2)
    else:
        return n

fib_string = '''
def fib(n: int):
    if n >= 2:
        return fib(n - 1) + fib(n - 2)
    else:
        return n
'''

if __name__ == '__main__':
    print([fib(n) for n in range(1, 11)])