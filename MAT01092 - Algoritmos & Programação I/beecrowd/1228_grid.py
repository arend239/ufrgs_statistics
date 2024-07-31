def grid(initial, pos_final):

    less = 0
    for i in range(1, len(initial)):
        j = i
        while j > 0 and pos_final[initial[j]] < pos_final[initial[j - 1]]:
            initial[j], initial[j - 1] = initial[j - 1], initial[j]
            less += 1
            j -= 1

    return less

while 1 == 1:
    try:
        n = int(input())
        ini = list(map(int, input().split()))
        fin = list(map(int, input().split()))

        pos_final = [0] * (n + 1)
        for i in range(n):
            pos_final[final[i]] = i

        print(grid(ini, pos_final))
    except EOFError:
        break

