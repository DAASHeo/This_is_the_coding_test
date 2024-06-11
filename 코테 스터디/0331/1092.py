import sys

n = int(sys.stdin.readline().strip())
limit = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
box_weight = list(map(int, sys.stdin.readline().strip().split()))

count = 0
limit.sort(reverse=True)
box_weight.sort(reverse=True)


if max(limit) < min(box_weight):
    print("-1")
    sys.exit()

else:
    while(len(box_weight) != 0):
        # 이중 for문 -> 시간초과 발생
        # for i in limit:
        #     if len(box_weight) != 0 and i < box_weight[-1]:
        #         continue
        #     for j in box_weight:
        #         if i >= j:
        #             box_weight.remove(j)
        #             break

        for i in range(n):
            if len(box_weight) != 0 and limit[i] < box_weight[-1]:
                continue
            for j in box_weight:
                if i >= j:
                    box_weight.remove(j)
                    break
        count += 1
    print(count)