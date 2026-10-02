nums = [3,5,2,6,7,8,1,4]

n = len(nums)

for i in range(1,n):
    key = nums[i]
    j = i-1
    while j >= 0 and nums[j] > key:
        nums[j+1] = nums[j]
        j -= 1
    nums[j+1] = key
print(nums)