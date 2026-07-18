n = input()

err = False
blacklist = {
    "0" : False,
    "1" : True,
    "2" : False,
    "3" : True,
    "4" : True,
    "5" : True,
    "6" : True,
    "7" : True,
    "8" : True,
    "9" : True,
}

result = ""

for i in range(len(n)):
    count = int(n[i])
    while not blacklist[str(count)]:
        if count > 9:
            err = True
            break
        count += 1
    blacklist[str(count)] = False
    if err:
        print(-1)
        break
    result += str(count)

print(int(result))
