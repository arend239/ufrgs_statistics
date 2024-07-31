while True:
    try:
        times = list(map(int, input().strip().split(' ')))
        if sum(times) == 0:
            break

        if((times[2] < times[0]) or (times[2] == times[0] and times[3] < times [1])):
            times[2] += 24

        print((times[2] * 60 + times[3]) - (times[0] * 60 + times[1]))

    except EOFError:
        break