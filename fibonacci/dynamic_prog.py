def fib(n: int):
    n_2 = 1
    n_1 = 1
    for _ in range(n - 1):
        n = n_1 + n_2
        n_2 = n_1
        n_1 = n
    return n_2

print([fib(n) for n in range(1, 11)])

fib_string ='''
def fib(n: int):
    n_2 = 1
    n_1 = 1
    for _ in range(n - 1):
        n = n_1 + n_2
        n_2 = n_1
        n_1 = n
    return n_2
'''