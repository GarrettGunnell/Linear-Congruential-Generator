import matplotlib.pyplot as plt

# MATLAB and FORTRAN rand
def lcg(seed):
    while True:
        seed = ((8121 * seed + 28411) % 134456)
        yield seed / 134456

# Non Generator, one time LCG
def lcg2(seed):
    return ((8121 * seed + 28411) % 134456) / 134456

rand = lcg(12398)
rngs = [next(rand) for _ in range(100000)]

plt.hist(rngs, bins=10, edgecolor='k', color = '#EE82EE', histtype = 'bar', rwidth = 0.92)
plt.xlim(0, 1)
plt.show()

