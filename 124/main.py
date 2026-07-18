n, arr = int(input()), list(map(int, input().split()))
memory, buffer = list([0]), 0

maximum = arr[0]

for i in range(n):
    buffer += arr[i]
    memory.append(buffer)
    if buffer > maximum:
        maximum = buffer
    if buffer < 0:
        buffer = 0



print(maximum)
