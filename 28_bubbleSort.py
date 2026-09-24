# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

#     return arr


# arr = [5, 1, 4, 2, 8]
# print(bubble_sort(arr))

# num = [5, 1, 4, 2, 8]
# n = len(num)
# for i in range(n-2,-1,-1):
#     for j in range(0,i+1):
#         if num[j] > num[j+1]:
#             num[j], num[j+1] = num[j+1], num[j]
# print(num)

num = [5, 1, 4, 2, 8]
n = len(num)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print(num)

