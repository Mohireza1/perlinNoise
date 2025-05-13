import random
import math

seeds = {}


def seed(x: int):
    if x in seeds:
        return seeds[x]
    seeds[x] = random.uniform(-1, 1)
    return seeds[x]


def interpolate(a, b, t: float):
    smooth_t = 6 * t**5 - 15 * t**4 + 10 * t**3
    return a + smooth_t * (b - a)


def noise(x):
    lx = math.floor(x)
    l_slope = seed(lx)
    r_slope = seed(lx + 1)
    t = x - lx
    a = l_slope * (t)
    b = r_slope * (t - 1)
    return interpolate(a, b, t)


i = 0
while i <= 2:
    print(f"{noise(i):.3f},")
    i += 0.01
