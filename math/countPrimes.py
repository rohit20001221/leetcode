import math

def countPrimes(n):
    isPrime = [True]*(n)
    isPrime[0] = isPrime[1] = False

    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if isPrime[i]:
            for j in range(i, n, i):
                if i != j:
                    isPrime[j] = False
    return sum(isPrime)

print(countPrimes(32))