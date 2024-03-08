n = input()
a = len([x for x in n.split("0") if x])
b = len([x for x in n.split("1") if x])

if a == 0 or b == 0:
    print("0")
else:
    print(min(a,b))
