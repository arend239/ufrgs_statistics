import random

# a) Create a function that generates a list with n random values between 1 and p.

def random_list(n,p):
    return [random.randint(0, p) for i in range(n)]

# b) Create a function that takes a list of random numbers and removes those divisible by 2 and 3.

def div_2_3(v):
    return [i for i in v if (i % 2 != 0 and i % 3 != 0)]

# c) Create a function sieve(n) that takes a value of n and returns a list with all prime numbers <= n. Use the Sieve of Eratosthenes for this.

def sieve(n):
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    n += 1
    is_prime = ([False] * 2) + [True for i in range(n - 2)]
    i = 2

    while(i**2 < n):
        if is_prime[i]:
            m = [x for x in range(i**2, n, i)]
            for j in m:
                is_prime[j] = False
        i += 1

    return [j for j, k in enumerate(is_prime) if k]

# d) Create a list L with n=100 random numbers between 1 and p=20. Create a list with the frequency of each number from 1 to p.
# e) Create a list L with n=100 random numbers between 1 and p=20. Remove duplicate numbers from the list.

def freq_list(v):
    l_count  = []
    l_unique = list(set(v))

    for i in l_unique:
        l_count.append(v.count(i))

    return dict(zip(l_unique, l_count))