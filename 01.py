inp = [l.strip() for l in open("input/01.txt").readlines()]


def p1():
    n = 50
    z = 0
    for i in inp:
        if i[0] == 'L':
            n = (n - int(i[1:])) % 100
        else:
            n = (n + int(i[1:])) % 100
        if n == 0:
            z += 1
    print(z)


def p2():
    n = 50
    z = 0
    for i in inp:
        dir = -1 if i[0] == 'L' else 1
        d = int(i[1:])
        for _ in range(d):
            n = (n + dir) % 100
            if n == 0:
                z += 1
    print(z)


if __name__ == "__main__":
    p1()
    p2()
