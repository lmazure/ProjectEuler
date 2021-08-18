candidate = 1
incr = 1
primes = []

def isPrime(number):
    for p in primes:
        if (number % p) == 0:
            return False
        if (p * p) > number:
            return True
    return True

while incr < 10002:
    candidate += 1
    if isPrime(candidate):
        print(f'{incr:6}: {candidate}')
        primes.append(candidate)
        incr += 1
