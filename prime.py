def isprime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    x = 5
    y = 2

    while x * x <= n:
        if n % x == 0:
            return False

        x += y
        y = 6 - y
    return True

for i in range(200):
    if i > 1 :
        if isprime(i) is True:
            print i
