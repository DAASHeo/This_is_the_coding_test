# d(n) 구현
def dn(n):
    n += sum(map(int, str(n)))
    return n

generated = set()
for i in range(1, 10001):
    generated.add(dn(i))

for i in range(1, 10001):
    if i not in generated:
        print(i)