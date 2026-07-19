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
    if r + 1 < n and arr[r] == x:
        return arr[r]
    elif r < n and arr[r] > x:
        return arr[r]
    else:
        return "NO SOLUTION"

for _ in range(m):
    x = int(input())
    print(task(x))