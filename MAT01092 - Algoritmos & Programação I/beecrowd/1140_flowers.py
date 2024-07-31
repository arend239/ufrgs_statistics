while True:
    try:
        inp = input().strip()
        if inp == '*' :
            break

        taut = 'Y'
        ws = inp.split()
        for w in ws:
            if w[0].lower() != ws[0][0].lower():
                taut = 'N'
                break

        print(taut)

    except EOFError:
        break