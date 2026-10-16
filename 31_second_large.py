# without sorting

nums = [55,32,100,97,-55,45,32,88,21]
n = len(nums)
largest = float("-inf")
s_large = float("-inf")
for i in range(0,n):
    if nums[i] > largest:
        s_large = largest
        largest= nums[i]

    elif nums[i] > s_large and nums[i] != largest:
        s_large = nums[i]
print(s_large)
