# N, M = map(int, input().split())

# list_ = []
# def dfs():
#     if len(list_) == M:
#         # print(f"{" ".join(map(str, list_))}")
#         # SyntaxError: f-string: expecting '}'
#         result = " ".join(map(str, list_))
#         print(result)
#         return
    
#     for i in range(1, N+1):
#         if i in list_:
#             continue
#         list_.append(i)
#         dfs()
#         list_.pop()

# dfs()
# ===========================================
# N, M = map(int, input().split())

# list_ = []
# def dfs():
#     if len(list_) == M and sorted(list_) == list_:
#         result = " ".join(map(str, list_))
#         print(result)
#         return
    
#     for i in range(1, N+1):
#         if i in list_:
#             continue
#         list_.append(i)
#         dfs()
#         list_.pop()

#         # if i in list_ or i <= max(list_):
#             # ValueError: max() arg is an empty sequence
#             # continue
#         # list_.append(i)
#         # dfs()
#         # list_.pop()

#         # try except...
#         # if i > max(list_):
#         #     ValueError: max() arg is an empty sequence
#         #     list_.append(i)
#         #     dfs()
#         #     list_.pop()

#         # if i > list_[len(list_)]:
#             # IndexError: list index out of range
#             # list_.append(i)
#             # dfs()
#             # list_.pop()

# dfs()
# ===================================================
