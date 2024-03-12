# list_ = []

# N = int(input())

# # for _ in range(N):
# # N번 하는 게 아니야!
#     x = int(input())

#     if x > 0:
#         list_.append(x)
#     else:
#         try:
#             print(list_.pop(min(list_)))
#         except ValueError: # 배열이 비어있는데 가장 작은 값을 출력할 경우 0 출력
#             print("0")

# list_A = [1, 2, 3, 4]
# print(list_A.pop())
# print(list_A)
# 4
# [1, 2, 3]
            
# 9                           
# 0
# 0
# 12345678
# 1
# 2
# 0
# 1
# 0
# Traceback (most recent call last):
#   File "1927_최소_힙.py", line 12, in <module>
#     print(list_.pop(min(list_)))
# IndexError: pop index out of range
# ========================================================
# list_ = []

# N = int(input())

# # for _ in range(N):
# # N번 하는 게 아니야!
# while 1:
#     x = int(input())

#     if x > 0:
#         list_.append(x)
#     else:
#         try:
#             print(list_.pop(min(list_)))
#             # IndexError: pop index out of range
#             # 아..? pop의 매개변수는 index구나
#             # 그럼 리무브를 쓸까?
#         except ValueError: # 배열이 비어있는데 가장 작은 값을 출력할 경우 0 출력
#             print("0")
# ==========================================================
# list_ = []

# N = int(input())

# # for _ in range(N):
# # N번 하는 게 아니야!
# while 1:
#     x = int(input())

#     if x > 0:
#         list_.append(x)
#     else:
#         try:
#             print(list_[-1])
#             # IndexError: list index out of range
#             list_.remove(min(list_))
#             # print(list_.pop(min(list_)))
#             # IndexError: pop index out of range
#             # 아..? pop의 매개변수는 index구나
#             # 그럼 리무브를 쓸까?
#         except ValueError: # 배열이 비어있는데 가장 작은 값을 출력할 경우 0 출력
#             print("0")
# =========================================================
list_ = []

N = int(input())

# for _ in range(N):
# N번 하는 게 아니야!
while 1:
    x = int(input())

    if x > 0:
        list_.append(x)
    else:
        try:
            print(list_[-1:-1:-1])
            # IndexError: list index out of range
            list_.remove(min(list_))

        except ValueError: # 배열이 비어있는데 가장 작은 값을 출력할 경우 0 출력
            print("0")