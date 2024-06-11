import sys
n = int(sys.stdin.readline())
array = []
dict = {}

for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()
number_list = sorted(list(set(array)))

for i in array:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

print(round(sum(array)/n))
print(array[n//2])

count_mode = max(dict.values())
mode = [k for k,v in dict.items() if v == count_mode]
mode.sort()

if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])

print(max(array) - min(array))