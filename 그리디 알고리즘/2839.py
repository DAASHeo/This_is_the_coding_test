n = int(input())
count = []
for i in range((n//3)+1):
    if (n - (3 * i)) % 5 == 0:
        count.append(i + (n - (3 * i)) // 5)
    elif 3 * i == n:
        count.append(i)

if len(count) == 0:
    print("-1")
else:
    print(min(count))