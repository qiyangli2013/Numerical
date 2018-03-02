import numpy as np
import pandas as pd
import time

# Uniform random number generator with LGM method
def unif(seed = None, N = 100):
    if seed == None:
        seed = time.time()

    a = 7**5
    b = 0
    m = 2 **31 - 1

    res= []
    res.append((a * seed + b) % m)

    for i in xrange(1,N):
        res.append((a * res[i - 1] + b) % m)

    return np.asarray(res) / float(m)

# bernoulli random number generator baed on LGM
def bern(p, seed = None, N = 100):
    # tmp = unif(seed, N)
    res = [0 if item > p else 1 for item in unif(seed, N)]
    return np.asarray(res)

# general discrete number generator
# correspond x and p need to in same order
def gene_disc(x, p,seed = None, N = 100):
    p_level = np.cumsum(p)
    res = []
    tmp = unif(seed, N)
    for i in xrange(N):
        # find first positive, correct position from generate p
        res.append(x[next(i for i, x in enumerate(p_level - tmp[i]) if x > 0)])

    return np.asarray(res)

# binomal distribution
# generate with two methods 1, recursion 2. expand from bernoulli
def binomal(n , p, seed = None, N = 100, method = 0):

    if method == 0:
        res = []

        for i in xrange(N):
            res.append(np.sum(bern(p,seed, n)))

        return np.asarray(res)
    else:
        return -1




# if __name__ == "__main__":

    # uniform
    # check with mean
    print np.mean(unif())
    print np.mean(unif(10, 1000))

    # bernoulli
    # check with mean
    print np.mean(bern(0.3))
    print np.mean(bern(0.3, 10, 1000))

    # general dsicrete distribution generator
    # check with mean
    x = np.asarray([1, 10, 7, 4, 5, 6])
    p = np.asarray([0.3, 0.25, 0.05, 0.1, 0.18, 0.12])
    print np.dot(x, p)
    print np.mean(gene_disc(x, p, 10, 10000))

    # binomal dsitribution generator
    # check with mean
    print np.mean(binomal(100, 0.36))
    print np.mean(binomal(100, 0.36, None, 10000))
