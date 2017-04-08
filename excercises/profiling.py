"""
1) Try using cProfileV:

    $ pip install cprofilev

Then run:

    $ python -m cprofilev excercises/profiling.py
    
and go to:

    http://localhost:4000/

This won't be very helpful here because it's by method, but you get the idea.
"""

def primes(n): 
    if n == 2:
        return [2]
    elif n < 2:
        return []
    
    s = range(3, n + 1, 2)
    mroot = n ** 0.5
    half = (n + 1) / 2 - 1
    
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m ** 2 - 3) / 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i += 1
        m = 2*i + 3

    return [2] + [x for x in s if x]

number = 10000000
elts = primes(number)
