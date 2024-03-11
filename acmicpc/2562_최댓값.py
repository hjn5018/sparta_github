list_ = []

for i in range(1, 10):
    test_case = int(input())
    list_.append(test_case)

# print(list_)
# [3, 29, 38, 12, 57, 74, 40, 85, 61]
    
max = 0
max_idx = 0
for j, num in enumerate(list_, 1):
#     print(j, num)
# 1 3
# 2 29
# 3 38
# 4 12
# 5 57
# 6 74
# 7 40
# 8 85
# 9 61
    if num > max:
        max = num
        max_idx = j

print(max)
print(max_idx)
