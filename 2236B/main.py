def task():
    n, k = map(int, input().split())
    s = list(map(int, input()))
    for i in range(n):
        if s[i] == 0:
            continue
        else:
            if i + k > n - 1:
                return False
            else:
                s[i + k] = 1 if s[i + k] == 0 else 0
    return True

n = int(input())
for _ in range(n):
    answer = task()
    print("yes" if answer else "no")
