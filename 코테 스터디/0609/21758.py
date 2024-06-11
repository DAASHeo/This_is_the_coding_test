import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

max_honey = 0

#벌꿀 양쪽, 벌통 중간 -> 벌꿀벌 -> i가 꿀통의 위치
for i in range(1, n-1):
    first = sum(array[1:i+1])
    second = sum(array[i:-1])
    max_honey = max(max_honey, first + second)

# 벌꿀 왼쪽, 벌통 오른쪽 -> 벌벌꿀 -> i가 두번째 벌꿀의 위치
for i in range(1, n):
    first = sum(array[1:]) - array[i]
    second = sum(array[i+1:])
    max_honey = max(max_honey, first + second)

# 벌꿀 오른쪽, 벌통 왼쪽 -> 꿀벌벌 -> i가 두번째 벌꿀의 위치
for i in range(1, n-1):
    first = sum(array[:-1]) - array[i]
    second = sum(array[:i])
    max_honey = max(max_honey, first + second)

print(max_honey)
