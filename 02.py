inp = [l.strip() for l in open("input/02.txt").read().split(",")]


def check(num: str):
    l = len(num)
    if l % 2 != 0:
        return False
    mid = l // 2
    return num[:mid] == num[mid:]


def check2(num: str):
    return num in (num + num)[1:-1]


p1 = 0
p2 = 0
for l, r in [l.split("-") for l in inp]:
    for n in range(int(l), int(r) + 1):
        if check(str(n)):
            p1 += n
        if check2(str(n)):
            p2 += n

print(p1)
print(p2)
