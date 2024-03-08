n, k = map(int, input().split())

count = 0
while(n % k != 0):
    n -= 1
    count += 1

while(n // k != 1):
    n = n // k
    count += 1

print(count+1)