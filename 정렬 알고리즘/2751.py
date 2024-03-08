#수 정렬하기2
import sys
n = int(sys.stdin.readline().strip())
answer = []
for _ in range(n):
    answer.append(int(sys.stdin.readline().strip()))

answer.sort()
for i in answer:
    print(i)