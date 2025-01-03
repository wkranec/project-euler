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
    # Use the Sieve of Eratosthenes
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    #
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is not a prime, else true.
    prime = [ True for i in range(n + 1) ]
    
    prime[0]= False
    prime[1]= False
    
    p = 2
    while (p * p <= n):
          
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
              
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        
        p += 1

    return [ p for p in range(n+1) if prime[p] ]