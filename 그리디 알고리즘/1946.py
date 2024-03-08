import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
    appliance = []
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        appliance.append(list(map(int, sys.stdin.readline().strip().split())))

    document = sorted(appliance, key= lambda score : score[0])

    pivot = document[0][1]
    picked = 1
    for i in range(1,len(document)):
        if pivot > document[i][1]:
            picked += 1
            pivot = document[i][1]

    print(picked)