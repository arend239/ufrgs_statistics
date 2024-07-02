# Pascal triangle

# by Stifel relation
def pascal_triangle_stifel(n):
    for l in range(n):
        line = []
        for i in range(l + 1):
            if i == 0 or i == l:
                line.append(1)
            else:
                line.append(prev_line[i - 1] + prev_line[i])
            print(line[i], end = ' ')
        print('')
        prev_line = line

pascal_triangle_stifel(5)

# by binomial
# C_{n,p} = \frac{n!}{p!(n-p)!}
def fact(x):
    if x <= 1:
        return 1
    return x * (fact(x - 1))

def pascal_triangle_binom(n):
    for i in range(n):
        for j in range(i + 1):
            print(fact(i) // (fact(j) * fact(i-j)), end=' ')
        print('')

pascal_triangle_binom(5)



