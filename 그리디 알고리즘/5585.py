n = 1000 - int(input())
count = 0

count += n // 500
n = n % 500
count += n // 100
n = n % 100
count += n // 50
n = n % 50
count += n // 10
n = n % 10
count += n // 5
n = n % 5
count += n // 1

print(count)

