# 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다.
# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.

# 1 ≤ n ≤ 1,000,000

def solution(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count
# n = 20
# for i in range(1, n):
#     if n % i == 0:
#         print(i)
# # 1
# # 2
# # 4
# # 5
# # 10
# ==================================
# n = 20
# for i in range(1, n):
#     if n % i == 0:
#         j = n // i
#         print(j)
# # 20
# # 10
# # 5
# # 4
# # 2
# ====================================
# n = 100
# for i in range(1, n):
#     if n % i == 0:
#         j = n // i
#         print(i, j)
# # 1 100
# # 2 50
# # 4 25
# # 5 20
# # 10 10
# # 20 5
# # 25 4
# # 50 2
# ===========================================
# n = 100
# for i in range(1, n+1):
#     if n % i == 0:
#         j = n // i
#         print((i, j))
# # (1, 100)
# # (2, 50)
# # (4, 25)
# # (5, 20)
# # (10, 10)
# # (20, 5)
# # (25, 4)
# # (50, 2)
# # (100, 1)
# ==============================================
# def solution(n):
#     for i in range(1, n+1):
#         if n % i == 0:
#             j = n // i
#             return (i, j)
        
# n = 100

# result = solution(n)

# print(result)
# # (1, 100)
# # while이 아니라 돌아가질 않는구나..
# # 가 문제가 아니라 result는 순서쌍 개수구낭!!
# ===================================================
# def solution(n):
#     for i in range(1, n+1):
#         while i == n:
#             if n % i == 0:
#                 j = n // i
#                 return (i, j)
        
# n = 100

# result = solution(n)

# print(result)
# # (100, 1)
# =================================================
n = 20
# 6
n = 100
# 9 
count = 0
for i in range(1, n+1):
    if n % i == 0:
        # j = n // i
        # print((i, j))
        count += 1
print(count)