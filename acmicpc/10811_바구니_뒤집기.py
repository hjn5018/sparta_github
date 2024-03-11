# N, M = map(int, input().split())

# bowl_list = [x for x in range(1, N+1)]
# # print(bowl_list)
# # [1, 2, 3, 4, 5]

# for _ in range(M):
#     i, j = map(int, input().split())

#     bowl_list[i-1:j] = bowl_list[i-1:j:-1]

# print(bowl_list)
# []
# =================================================
# N, M = map(int, input().split())

# bowl_list = [x for x in range(1, N+1)]

# for _ in range(M):
#     i, j = map(int, input().split())

#     bowl_list[i-1:j] = bowl_list[i-1:j:-1]
#     print(bowl_list)
# 5 4
# 1 2
# [3, 4, 5]
# 3 4
# [3, 4]
# 1 4
# []
# 2 2
# []
# =================================================
# N, M = map(int, input().split())

# bowl_list = [x for x in range(1, N+1)]

# for _ in range(M):
#     i, j = map(int, input().split())

#     bowl_list[i-1:j]
#     print(bowl_list)
# 5 4
# 1 2
# [1, 2, 3, 4, 5]
# 3 4
# [1, 2, 3, 4, 5]
# 1 4
# [1, 2, 3, 4, 5]
# 2 2
# [1, 2, 3, 4, 5]
# ========================================
# N, M = map(int, input().split())

# bowl_list = [x for x in range(1, N+1)]

# for _ in range(M):
#     i, j = map(int, input().split())

#     bowl_list.pop([i-1:j]).reverse().insert(i-1)
# SyntaxError: invalid syntax
# ===================================================
# N, M = map(int, input().split())

# bowl_list = [x for x in range(1, N+1)]

# for _ in range(M):
#     i, j = map(int, input().split())

#     bowl_list[i-1:j] = bowl_list[i-1:j:-1]
#     print(bowl_list)
# 5 4
# 1 2
# [3, 4, 5]
# 3 4
# [3, 4]
# 1 4
# []
# 2 2
# []
# =================================================
# N, M = map(int, input().split())

# bowl_list = [x for x in range(1, N+1)]

# print(bowl_list)
# # [1, 2, 3, 4, 5]

# bowl_list[1:2] = bowl_list[1:2:-1]

# print(bowl_list)
# # [1, 3, 4, 5]
# ======================================
# N, M = map(int, input().split())

# bowl_list = [x for x in range(1, N+1)]

# print(bowl_list)
# # [1, 2, 3, 4, 5]

# bowl_list[1:3] = bowl_list[1:3:-1]

# print(bowl_list)
# # [1, 4, 5]
# ===========================================
# N, M = map(int, input().split())

# bowl_list = [x for x in range(1, N+1)]

# print(bowl_list)
# # [1, 2, 3, 4, 5]

# print(bowl_list[1:3])
# # [2, 3]
# print(bowl_list[1:3:-1])
# # []
# print(bowl_list[1:3][::-1])
# # [3, 2]
# print(bowl_list)
# # [1, 2, 3, 4, 5]
# ============================================
N, M = map(int, input().split())

bowl_list = [x for x in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())

    bowl_list[i-1:j] = bowl_list[i-1:j][::-1]
    # print(bowl_list)
# 5 4
# 1 2
# [2, 1, 3, 4, 5]
# 3 4
# [2, 1, 4, 3, 5]
# 1 4
# [3, 4, 1, 2, 5]
# 2 2
# [3, 4, 1, 2, 5]
print(" ".join([str(x) for x in bowl_list]))
# 3 4 1 2 5