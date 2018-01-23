def fib(n):
    '''
    Returns the nth number in the fibonacci sequence
    '''

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


def fib_from(_from, _to):
    a, b = 0, 1
    while b != _from:
        a, b = b, a + b

    print(b)
    # a is the number previous to _from
    for _ in range(_to):
        a, b = b, a + b
        print(b, end=' ')


if __name__ == '__main__':
    num = int(input())
    iters = int(input())

    fib_from(num, iters)
