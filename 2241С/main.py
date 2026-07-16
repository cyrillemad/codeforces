def task():
    n = int(input())
    s = list(map(int, input()))
    blocks = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            blocks += 1

    if blocks == 2:
        return 2
    else:
        return 1

n = int(input())
for _ in range(n):
    print(task())