# method 1
nums = [55,35,-97,99,3,67,100]
n = len(nums)
large = nums[0]
for i in range(0,n):
    large = max(large, nums[i])
print(large)

# method 2

for j in range(0,n):
    if nums[j] > large:
        large = nums[j]
print(large)