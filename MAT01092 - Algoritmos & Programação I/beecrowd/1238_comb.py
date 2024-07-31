def comb(ws):
    a, b, c = ws[0], ws[1], ''
    for j,k in zip(a,b):
        c += j + k
    c += a[len(b):] if len(a) > len(b) else b[len(a):]
    return c

n = int(input())

for i in range(n):

    char = input().split()
    print(comb(char))
