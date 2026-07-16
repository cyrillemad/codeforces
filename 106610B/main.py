a, k = int(input()), int(input())

need = k * (k + 1) // 2
if k > a or need > a * a:
    print("Impossible")
else:
    print(a * a - need)