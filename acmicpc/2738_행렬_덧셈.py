"""
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100
"""
# N, M = map(int, input().split())

# matrix_a = []
# matrix_b = []
# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_a.append(row)
# # print(matrix_a)
# # [[1, 1, 1], [2, 2, 2], [0, 1, 0]]
# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_b.append(row)

# new_matrix = []
# for i in range(N):
#     for j in range(M):
#         new_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]

# print(new_matrix)
# IndexError: list index out of range
# ===================================================
# N, M = map(int, input().split())

# matrix_a = []
# matrix_b = []
# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_a.append(row)
# # print(matrix_a)
# # [[1, 1, 1], [2, 2, 2], [0, 1, 0]]

# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_b.append(row)
# # print(matrix_b)
# # [[3, 3, 3], [4, 4, 4], [5, 5, 100]]
    
# new_matrix = [[], [], []]
# for i in range(N):
#     for j in range(M):
#         new_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]

# # print(new_matrix)
# # IndexError: list assignment index out of range
# ======================================================================
# N, M = map(int, input().split())

# matrix_a = []
# matrix_b = []
# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_a.append(row)

# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_b.append(row)
    
# # new_matrix = [[], [], []]
# new_matrix = []
# for i in range(N):
#     for j in range(M):
#         # new_matrix[i][j] += matrix_a[i][j] + matrix_b[i][j]
#         new_matrix[i][j].append(matrix_a[i][j] + matrix_b[i][j]) 
        
#         # new_matrix[i][j] = 0
# # print(new_matrix)
# # NameError: name 'new_matrix' is not defined
    
# # new_matrix = [[], [], []]
# # for i in range(N):
# #     new_matrix.append()
# ==============================================================
# N, M = map(int, input().split())

# for _ in range(N):
#     row = list(map(int, input().split()))

# list_ = [0]*3
# [0, 0, 0]

# list_1 = list_*3
# [0, 0, 0, 0, 0, 0, 0, 0, 0]

# list_1 = []
# list_1.append(list_)
# [[0, 0, 0]]

# list_1 = []
# list_1.append(list_) * 3
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

# list_1 = []
# list_1.append(list_)
# list_1.append(list_)
# list_1.append(list_)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# list_1 = []
# for _ in range(3):
    # list_1.append(list_)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# print(list_1)
# ====================================================
# N, M = map(int, input().split())

# matrix_a = []
# matrix_b = []
# matrix_c = []

# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_a.append(row)
# # print(matrix_a)
# # [[1, 1, 1], [2, 2, 2], [0, 1, 0]]
    
# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_b.append(row)
# # print(matrix_b)
# # [[3, 3, 3], [4, 4, 4], [5, 5, 100]]

# for _ in range(N):
#     matrix_c.append([0]*3)
# # print(matrix_c)
# # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for i in range(N):
#     for j in range(M):
#         matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]
# print(matrix_c)
# # [[4, 4, 4], [6, 6, 6], [5, 6, 100]]
# 런타임 에러 (indexError)
# ===============================================
# N, M = map(int, input().split())

# matrix_a = []
# matrix_b = []

# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_a.append(row)

    
# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_b.append(row)

# for i in range(N):
#     for j in range(M):
#         matrix_a[i][j] += matrix_b[i][j]
# print(matrix_a)
# [[4, 4, 4], [6, 6, 6], [5, 6, 100]]
# 틀렸습니다 ?????
# 워워 진정해.
# 출력 조건에 맞게 출력하자 ^^
# ===========================================================
# N, M = map(int, input().split())

# matrix_a = []
# matrix_b = []

# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_a.append(row)

    
# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_b.append(row)

# for i in range(N):
#     for j in range(M):
#         matrix_a[i][j] += [matrix_b[i][j]]
# # TypeError: unsupported operand type(s) for +=: 'int' and 'list'
# =================================================================
# a = [2]
# b = [3]
# print(a + b)
# # [2, 3]

# print(a += b)
# # SyntaxError: invalid syntax

# a += b
# print(a)
# # [2, 3]

# a[0]+=b[0]
# print(a)
# # [5]
# ========================================
# N, M = map(int, input().split())

# matrix_a = []
# matrix_b = []

# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_a.append(row)

    
# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_b.append(row)

# for i in range(N):
#     for j in range(M):
#         matrix_a[i][j] += matrix_b[i][j]
# # print(matrix_a)
# # [[4, 4, 4], [6, 6, 6], [5, 6, 100]]

# # for i in range(N):
# #     " ".join(matrix_a[i])
# # TypeError: sequence item 0: expected str instance, int found    
# # print(matrix_a)
# ===========================================
# N, M = map(int, input().split())

# matrix_a = []
# matrix_b = []

# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_a.append(row)

    
# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix_b.append(row)

# for i in range(N):
#     for j in range(M):
#         matrix_a[i][j] += matrix_b[i][j]
# # print(matrix_a)
# # [[4, 4, 4], [6, 6, 6], [5, 6, 100]]

# for i in range(N):
#     matrix_a[i] = " ".join(str(x) for x in matrix_a[i])

# print(matrix_a)
# # ['4 4 4', '6 6 6', '5 6 100']
# ====================================================
N, M = map(int, input().split())

matrix_a = []
matrix_b = []

for _ in range(N):
    row = list(map(int, input().split()))
    matrix_a.append(row)

    
for _ in range(N):
    row = list(map(int, input().split()))
    matrix_b.append(row)

for i in range(N):
    for j in range(M):
        matrix_a[i][j] += matrix_b[i][j]
# print(matrix_a)
# [[4, 4, 4], [6, 6, 6], [5, 6, 100]]

for i in range(N):
    matrix_a[i] = " ".join(str(x) for x in matrix_a[i])

for i in range(N):
    print(f"{matrix_a[i]}")
# 4 4 4
# 6 6 6
# 5 6 100