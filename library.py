## Module of Python functions utilized across various solutions.

def digits(integer):
    return [ int(x) for x in str(integer) ]

def is_prime(n):
    if n % 2 == 0:
        return False
        
    for i in range(3, int(n**0.5)+2, 2):
        if n % i == 0:
            break
    else:
        return True

    return False

def primes_up_to(n):
    if n <= 2:
        raise StopIteration
    yield 2
    for i in range(3, n, 2):
        for x in range(3, int(i**0.5)+2, 2):
            if not i % x:
                break
        else:
            yield i