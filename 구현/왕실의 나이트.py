x, y = input()
y = int(y)
x = (ord(x) - ord('a'))+1

move = [(2, 1), (2, -1), (-2, -1), (-2, 1), (1, 2), (-1, 2), (1,-2), (-1, -2)]
count = 0

for a,b in move:
    if 0 < (x + b) <= 8 and 0 < (y + a) <= 8:
        count += 1
    else:
        pass

print(count)