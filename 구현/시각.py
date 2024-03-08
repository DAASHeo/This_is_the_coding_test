n = int(input())

count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if('3' in str(second) or '3' in str(minute) or '3' in str(hour)):
                count += 1
            second = k
        minute = j
    hour = i

print(count)