nums = list(map(int, input()[1:-1].split(",")))
k = 0
temp = 0

for i in range(len(nums)):
    if nums[i] != 0:
        temp = nums[k]
        nums[k] = nums[i]
        nums[i] = temp
        k += 1

print(nums)