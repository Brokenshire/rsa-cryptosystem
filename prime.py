# Copyright 2020 Jack Brokenshire

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Third-party import(s)
import random


def is_prime(n):
    """ Fermat primality test.

    >>> is_prime(0)
    False
    >>> is_prime(2)
    True
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False

    Args:
        n (int): Value to be tested for primality.

    Returns:
        boolean: True if n is a prime number, otherwise, False.
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_of_eratosthenes(n):
    """ Algorithm to compute a list of prime numbers.

    >>> sieve_of_eratosthenes(10)
    [2, 3, 5, 7]
    >>> sieve_of_eratosthenes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]

    Returns:
        list: A list containing prime numbers.
    """
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    return primes


def generate_small_prime(size):
    """ Chooses a random prime generated from the Sieve of Eratosthenes.
    
    >>> n = generate_small_prime(10)
    >>> is_prime(n - 1)
    False
    >>> is_prime(n)
    True
    >>> is_prime(n + 1)
    False

    Args:
        size (int): The max limit for prime generation.

    Returns:
        int: A prime number.
    """
    primes = sieve_of_eratosthenes(size)
    return random.choice(primes)


def generate_big_prime(size):
    """[summary]

    Args:
        size (int): The max limit for prime generation.

    Returns:
        [type]: [description]
    """
    # not built yet...
    n = 0
    return n
    

def generate_p_and_q(size):
    """ Gets the values of p and q determined by the size of the prime wanted.

    >>> p, q = get_p_and_q(100)
    >>> is_prime(p - 1)
    False
    >>> is_prime(q - 1)
    False
    >>> is_prime(p)
    True
    >>> is_prime(q)
    True
    >>> is_prime(p + 1)
    False
    >>> is_prime(q + 1)
    False

    Args:
        size (int): The range in which the primes can be generated within.

    Returns:
        int: Two prime values p and q used for the RSA crpytosystem.

    Note:
        Need to make sure p and q are distinct.
    """
    if size < 200:
        p = generate_small_prime(size)
        q = generate_small_prime(size)
    else:
        p = generate_big_prime(size)
        q = generate_big_prime(size)
    return p, q


if __name__ == "__main__":
    import doctest
    doctest.testmod()