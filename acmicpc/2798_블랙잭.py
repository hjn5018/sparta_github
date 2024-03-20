# N, M = map(int, input().split())

# L = list(map(int, input().split()))
# print(N, M, L)
# 5 21                                          
# 5 6 7 8 9
# 5 21 [5, 6, 7, 8, 9]

# list_ = []
# for i in range(len(L)):
#     del L[i]
#     print(L)
#     for j in range(len(L)):
#         del L[j]
        # IndexError: list assignment index out of range
#         for k in range(len(L)):
#             if L[i] + L[j] + L[k] < M:
#                 list_.append(L[i] + L[j] + L[k])
# print(max(list_))

# while True:
    
# ==================================
# list_ = [1,2,3,4,5]
# del list_[1]
# print(list_)
# [1, 3, 4, 5]
# ==============================
# N, M = map(int, input().split())

# L = list(map(int, input().split()))

# sum = 0
# sum += max(L)

# max_idx = L.index(max(L))
# L = L[:max_idx] + L[max_idx+1: ]
# sum += max(L)

# if sum >= M:
#     pass # 폐기, 36~40 반복
# else:
#     pass # 36 ~ 38 반복
        
# ==============================
# N, M = map(int, input().split())

# L = list(map(int, input().split()))


# list_ = []
# for i in range(len(L)):
#     sum = 0
#     sum += L[i]
#     print(f"{sum=}")
#     L1 = L[:i] + L[i+1:]
#     for j in range(len(L1)):
#         sum += L[j]
#         # print(sum)
#         L2 = L1[:j] + L1[j+1:]
#         for k in range(len(L2)):
#             sum += L[k]
#             # print(sum)
#             if sum < M:
#                 list_.append(sum)
# # print(list_)
# # 5 21
# # 5 6 7 8 9
# # [15]

# # 10 500
# # 93 181 245 214 315 36 185 138 216 295
# # [279, 460]

# # print(max(list_))
# ==========================================
N, M = map(int, input().split())

L = list(map(int, input().split()))

