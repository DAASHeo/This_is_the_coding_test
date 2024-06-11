# count = (start+1)*(end+1)
n, k = input().split()
n = int(n)
k = int(k)

start = 0 #(가로)
end = n #(세로)

while start <= end:
    row =
    if start == 0 and end == 0:
        start += 1
        count += 1
    if k % 2 != 0 and count % 2 != 0:
        end += 1
        count *= 2
    count = (start+1)*(end+1)

if count == k :
    print("YES")
else:
    print("NO")