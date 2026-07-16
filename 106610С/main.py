n, k, x = map(int, input().split())
a, b, c = 0, 0, 0

while a + b + c < k:
    steps = a + b + c
    prod = 5 * a + 3 * b + c
    if k - steps == x - prod:
        c += 1
    elif (x - prod - k - steps) % 3 == 0:
        b += 1
    elif c < n :
        a += 1
    else:
        c += 1

print(a, b, c)