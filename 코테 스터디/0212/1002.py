# import math
# def solution(x1, y1, r1, x2, y2, r2):
#     d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#     if d == 0 and r1 == r2:
#         return -1
#     elif d > r1 + r2 or d < abs(r1 - r2):
#         return 0
#     elif d == r1 + r2 or d == abs(r1 - r2):
#         return 1
#     else:
#         return 2
#
# # 입력 받는 부분
# def main():
#     T = int(input())
#     for _ in range(T):
#         x1, y1, r1, x2, y2, r2 = map(int, input().split())
#         print(solution(x1, y1, r1, x2, y2, r2))
#
# main()
