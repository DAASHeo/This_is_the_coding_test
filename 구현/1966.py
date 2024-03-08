from collections import deque
def printer():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = deque(a)
    count = 0
    while a:
        if m == -1:
            m = len(a) - 1
        if a[0] == max(a):
            if m == 0:
                count += 1
                return print(count)
            else:
                a.popleft()
                m -= 1
                count += 1
        else:
            a.rotate(-1)
            m -= 1


def main():
    t = int(input())
    for _ in range(t):
        printer()

main()