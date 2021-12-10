# reverse fatorization

import array


def findMinimalState(n: int, k: int,numbers: set):
    n_multiples = []
    for i in range(2, n/2):
        if n % i == 0:
            n_multiples.append(i)
    
    