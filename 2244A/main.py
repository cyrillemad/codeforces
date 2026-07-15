def task():
    _ = int(input())
    s = input()
    answer = 0
    count = 0

    for c in s:
        if c == '#':
            count += 1
        else:
            if count:
                answer = max(answer, (count + 1) // 2)
            count = 0
    if count:
        answer = max(answer, (count + 1) // 2)
    print(answer)

n = int(input())
for _ in range(n):
    task()