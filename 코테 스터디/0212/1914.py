# def solution(n, first, second, third):
#     count = 0
#     while(len(third) != n):
#         if len(third) == 0:
#             third.append(first[0])
#             del first[0]
#         elif len(second) == 0:
#             second.append(first[0])
#             del first[0]
#         count += 1
#     return count
#
# def main():
#     N = int(input())
#     first = [i for i in range(1, N+1)]
#     first.reverse()
#     print(first)
#     second = []
#     third = []
#     solution(N, first, second, third)
#
# main()