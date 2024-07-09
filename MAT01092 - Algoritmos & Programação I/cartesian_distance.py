# Create a set S with n randomly selected ordered pairs of points (x, y) in the Cartesian plane within the range (0,10) x (0,10).

# a) Find the two points in S that are farthest apart.
# b) Find the two points in S that are closest together.
# c) Calculate the average distance between all pairs of points in S.

import random
import itertools

def random_cart_points(n):
    S = set()

    for i in range(n):
        S.add((random.randint(0, 10), random.randint(0, 10)))

    return S

def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(0.5)

S = random_cart_points(3)
comb = list(itertools.combinations(S, 2))
comb = [(i, j, distance(i, j)) for (i, j) in comb]

# Answers
max(comb, key=lambda x: x[2])
min(comb, key=lambda x: x[2])
sum(k for i, j, k in comb)/len(comb)