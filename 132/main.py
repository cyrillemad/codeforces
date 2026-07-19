n, m = map(int, input().split())
arr = list(map(int, input().split()))

l, r = -1, n
mid = -1
for i in range(m):
    mid = (l + r) // 2
    if arr[i] == 0:
        l = mid
    else:
        r = mid

print(r)