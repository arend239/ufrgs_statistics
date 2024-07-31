while 1 == 1:

    n = input().strip()
    if n.startswith('-'):
        break

    try:
        n = hex(int(n))
        print(n[:2] + n[2:].upper())
    except ValueError:
        print(int(n, 16))