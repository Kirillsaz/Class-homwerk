from itertools import islice

def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
        yield res

n = 10

for el in islice(fact(n), n):
    print(el)
