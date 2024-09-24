numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            primes = numbers
NotPrimes = (set(not_primes))
primes = [x for x in numbers if x not in not_primes]
for i in primes:
    if i == 1:
        primes.remove(1)
print('primes: ', primes)
print('NotPrimes: ',list(NotPrimes))