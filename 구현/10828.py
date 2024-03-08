import sys

n = int(sys.stdin.readline().strip())

stack = []

for i in range(n):
    order = sys.stdin.readline().strip().split()
    if (len(order)) == 2:
        numb = int(order[1])
        order = order[0]
    else:
        order = order[0]

    if order == "push":
        stack.append(numb)

    elif order == "pop":
        if len(stack) >= 1:
            print(stack.pop())
        else:
            print("-1")

    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) >= 1:
            print("0")
        else:
            print("1")
    else:
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print("-1")