""" 라이브러리 ver.
import itertools

def main():
    N, M = map(int, input().split())
    arr = list(input().split())
    arr.sort()
    result = itertools.permutations(arr, M)

    for perm in result:
        print(' '.join(perm))

"""
""" 중복일 경우 이 코드에서 변형이 필요함
n,m = map(int, input().split())
nums = list(map(int,input().split()))
nums.sort()
list = []

def sol(key):
    if key == m:
        return print(' '.join(map(str, list)))
    for i in nums:
        if i not in list:
            list.append(i)
            sol(key+1)
            list.pop()
        
sol(0)
"""

