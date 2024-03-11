# N, M = map(int, input().split())

# # bowl_list = [x for x in range(1, N+1)]

# # print(bowl_list)
# # [1, 2, 3, 4, 5]

# bowl_list = []
# for i in range(1, N+1):
#     bowl_list[i] = i
# # IndexError: list assignment index out of range
# print(bowl_list)

# for _ in range(M):
#     i, j = map(int, input().split())
# =============================================
# N, M = map(int, input().split())

# bowl_list = []
# for i in range(N):
#     bowl_list.append(i+1)

# # print(bowl_list)
# # [1, 2, 3, 4, 5]

# for _ in range(M):
#     i, j = map(int, input().split())

#     empty = bowl_list[i]
#     bowl_list[i] = bowl_list[j]
#     bowl_list[j] = empty

# print(bowl_list)
# # [1, 4, 2, 5, 3]
# # 한 칸씩 밀린 듯
# ================================================
N, M = map(int, input().split())

bowl_list = []
for i in range(N):
    bowl_list.append(i+1)

# print(bowl_list)
# [1, 2, 3, 4, 5]

for _ in range(M):
    i, j = map(int, input().split())

    empty = bowl_list[i-1]
    bowl_list[i-1] = bowl_list[j-1]
    bowl_list[j-1] = empty

# print(bowl_list)
# [3, 1, 4, 2, 5]
    
print(" ".join([str(x) for x in bowl_list]))
# 3 1 4 2 5