# N, X = map(int, input().split())

# A = list(map(int, input().split()))

# list_ = []

# for num in A:
#     if num < 5:
#         list_.append(num)

# print(list_)
# [1, 4, 2, 3]

# print(" ".split(list_))
# ???

# print(" ".join(list_))
# TypeError: sequence item 0: expected str instance, int found
# =============================================
# N, X = map(int, input().split())

# A = list(map(int, input().split()))

# list_ = []

# for num in A:
#     if num < 5:
#         list_.append(str(num))

# print(" ".join(list_))
# 1 4 2 3

# 틀렸습니다.
# ===============================
N, X = map(int, input().split())

A = list(map(int, input().split()))

list_ = []

for num in A:
    if num < X:
        list_.append(str(num))

print(" ".join(list_))