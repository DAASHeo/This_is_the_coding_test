n = int(input())

answer = []

for _ in range(n):
    a, b = input().split()
    answer.append([a,int(b)])

answer = sorted(answer, key=lambda student : student[1])

for student in answer:
    print(student[0], end=" ")