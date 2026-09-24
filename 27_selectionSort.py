# num = [8,4,6,9,2,7]
# n=len(num)
# for i in range(0,n):
#     min_index = i
#     for j in range(i+1,n):
#         if num[j]<num[min_index]:
#             min_index=j
#     num[i],num[min_index]=num[min_index],num[i]

# print(num)

# num = [2,4,6,2,5,3,8]
# n = len(num)
# for i in range(0,n):
#     min_index = i
#     for j in range(i+1, n):
#         if num[j]<num[min_index]:
#             min_index = j
#     num[i],num[min_index] = num[min_index], num[i]
# print(num)


num = [2,7,4,9,1]
n = len(num)
for i in range(0 , n):
    min = i
    for j in range(i+1, n):
        if num[j] < num[min]:
            min = j
    num[i], num[min] = num[min], num [i]
print(num)        