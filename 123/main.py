n, q = map(int, input().split())
arr = list(map(int, input().split()))

memory = list([0])
buffer = 0
for i in range(1, n + 1):
    buffer += arr[i - 1]
    memory.append(buffer)

for i in range(q):
    l, r = map(int, input().split())
    print(memory[r] - memory[l - 1])