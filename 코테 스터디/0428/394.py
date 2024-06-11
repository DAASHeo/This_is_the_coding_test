import sys
# isdigit => 숫자 판별 네소드
s = list((sys.stdin.readline().strip()))
number_list = []
str_list = []
open_index = []
n = 0
x = 0
y = 0

for i in range(len(s)):
    if s[i] == "[":
        open_index.append(i)
    elif s[i] == "]":
        n = open_index.pop()
        slice = ''.join(str_list[-(i - n - 1)])
        str_list = [x for x in str_list if x not in slice]
        x = number_list.pop()
        str_list.append(slice*x)
    else:
        if s[i].isdigit() == True:
            number_list.append(int(s[i]))
        else:
            str_list.append(s[i])

print(''.join(str_list))