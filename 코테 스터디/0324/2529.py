import sys
n = int(input())
sign = list(map(str, sys.stdin.readline().strip().split()))

visited = [0]*10 # 0~9까지의 정수 방문 여부
max_ans = ""
min_ans = ""


def check(i,j,k):
    if k == "<":
        return i < j
    else:
        return i > j
def solution(depth, s):
    global max_ans, min_ans

    if depth