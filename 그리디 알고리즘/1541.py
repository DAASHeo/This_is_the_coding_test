n = input().split("-")
answer = []
result = 0

for i in range(len(n)) :
    if "+" in n[i]:
        answer.append(sum(list(map(int, n[i].split("+")))))

    else:
        answer.append(int(n[i]))


if len(answer) == 0:
    print(answer[0])
else:
    result = answer[0]
    for i in range(1, len(answer)):
        result -= answer[i]
    print(result)