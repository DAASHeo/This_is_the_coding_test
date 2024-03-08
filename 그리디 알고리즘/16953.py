a, b = map(int, input().split())
flag = False
count = 0

while (b > a):
    if str(b)[-1] == '1':
        b = int(str(b)[:-1])
        count += 1

    elif a == b:
        break

    elif b % 2 == 0:
        b = b // 2
        count += 1

    else:
        break

if a == b:
    print(count+1)

else:
    print("-1")