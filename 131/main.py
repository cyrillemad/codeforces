n, m = map(int, input().split())

def task(k):
    step = 0
    l, r = -1, n
    while (l + 1 < r):
        step += 1
        mid = (l + r) // 2
        if mid < k:
            l = mid
        else:
            r = mid
    return step

for i in range(m): print(task(int(input())))
