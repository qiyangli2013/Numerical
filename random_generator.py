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
def bern(seed = None, N = 100):
    # tmp = unif(seed, N)
    res = [1 if item > 0.5 else 0 for item in unif(seed, N)]
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


# if __name__ == "__main__":

    # uniform
    # check with mean
    print np.mean(unif())
    print np.mean(unif(10, 1000))

    # bernoulli
    # check with mean
    print np.mean(bern())
    print np.mean(bern(10, 1000))

    myList = [0.0 , .1, -.1, .05, 2.0]

    next(i for i, x in enumerate(myList) if x > 0)
