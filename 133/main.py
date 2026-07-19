n, m = map(int, input().split())
arr = list(map(int, input().split()))

def task(x):
    l, r = -1, n
    while l + 1 < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid
        else:
            r = mid
    return r < n and arr[r] == x

for _ in range(m):
    x = int(input())
    print("YES" if task(x) else "NO")