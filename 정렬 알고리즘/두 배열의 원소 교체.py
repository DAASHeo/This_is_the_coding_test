n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0

a.sort()
b.sort(reverse=True)

for i in range(len(a)):
    if count == k:
        break
    if a[i] < b[i]:
        a[i] = b[i]
        count += 1

print(sum(a))