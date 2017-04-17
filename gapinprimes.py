g = 10
m = 300
n = 400
def gap(g, m, n):
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

    primes = []
    for i in range(m,n):
        if i > 1 :
            if isprime(i) is True:
                primes.append(i)
    print primes
    for i in range(len(primes)):
        if i > 0:
            if primes[i] - primes[i-1] == g:
                return [primes[i-1], primes[i]]
                break







print gap(g, m, n)

#Test.assert_equals(gap(2,100,110), [101, 103])
