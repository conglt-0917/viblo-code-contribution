def fib(n):
    if n < 0:
        return (-1)**(n % 2 + 1) * fib(-n)
    a, b, p, q = (1, 0, 0, 1)
    while n != 0:
        if (n % 2) == 0:
            (p, q) = (p * p + q * q,
                      (2 * p + q) * q)
            n /= 2
        else:
            (a, b) = ((b + a) * q + a * p,
                      b * p + a * q)
            n -= 1
    return b


n = int(input())
print(fib(n))
