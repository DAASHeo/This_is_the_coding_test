n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

start = 0
end = n - 1
answer = abs(liquid[start]+liquid[end])
final = [liquid[start],liquid[end]]

while start < end:
    interval_sum = liquid[start] + liquid[end]
    if answer > abs(interval_sum):
        answer = abs(interval_sum)
        final = [liquid[start], liquid[end]]
        if answer == 0:
            break
    if interval_sum < 0: #0과 가깝게 만들기 위해
        start += 1
    else:
        end -= 1
print(final[0], final[1])

