n = int(input())
cur, a, b = map(int, input().split())
mod = 1791791791

max1 = -1
max2 = -1

pos1 = -1
pos2 = -1

for i in range(1, n + 1):
    cur = (cur * a + b) % mod

    if cur > max1:
        max2 = max1
        pos2 = pos1

        max1 = cur
        pos1 = i

    elif cur > max2:
        max2 = cur
        pos2 = i

print(pos1, pos2)