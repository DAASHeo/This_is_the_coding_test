import sys
input = sys.stdin.readline().strip()

n = int(input)
dice = list(map(int, input.split()))
sum = 0
sumLists = []

if(n == 1):
    dice = sorted(dice)
    for i in range(0,5):
        sum += dice[i]
else:
    sumLists.append(min(dice[0],dice[5]))
    sumLists.append(min(dice[1],dice[4]))
    sumLists.append(min(dice[2],dice[3]))
    sumLists = sorted(sumLists)

    min1 = sumLists[0]
    min2 = sumLists[0] + sumLists[1]
    min3 = sumLists[0] + sumLists[1] + sumLists[2]

    n1 = (n-2)*(n-2) + 4*(n-1)*(n-2)
    n2 = 4*(n-2) + 4*(n-1)
    n3 = 4

    sum += n1 * min1
    sum += n2 * min2
    sum += n3 * min3

print(sum)