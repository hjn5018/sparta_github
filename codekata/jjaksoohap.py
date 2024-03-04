# 내 최종 답안
def solution(n):
    empty_list=[]
    for i in range(0, n+1, 2):
        empty_list.append(i)
    add_num = 0
    for num in empty_list:
        add_num += num
    return add_num
# =========================================
# # 시도 1
# def solution(n):
#     empty_list=[]
#     for i in range(n)
#     # SyntaxError: invalid syntax
#     # for문에 콜론 빼먹음
#         empty_list.append(i)
#     return empty_list
# ======================================
# # 시도 2
# def solution(n):
#     empty_list=[]
#     for i in range(n):
#         empty_list.append(i)
#     return empty_list
# # 0부터 n-1까지의 리스트가 생성됨.
# ========================================
# # 시도 3
# def solution(n):
#     empty_list=[]
#     for i in range(n,1):
#         empty_list.append(i)
#     return empty_list

# result = solution(9)

# print(result)
# # []
# # range(start, stop, step)
# ==========================================
# # 시도 4
# def solution(n):
#     empty_list=[]
#     for i in range(1, n):
#         empty_list.append(i)
#     return empty_list

# # result = solution(9)
# # # [1, 2, 3, 4, 5, 6, 7, 8]

# # result = solution(10)
# # # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # n이 짝수 일 때 n 포함이 안됨 -> range(n+1) 필요

# print(result)
# ===========================================
# # 시도 5
# def solution(n):
#     empty_list=[]
#     for i in range(1, n+1):
#         empty_list.append(i)
#     return empty_list

# # print(solution(9))
# # # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(solution(10))
# # # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # 원하는 리스트는 만들었고, 조금 더 조작해보기
# =============================================
# # 시도 6
# def solution(n):
#     empty_list=[]
#     for i in range(2, n+1):
#         empty_list.append(i)
#     return empty_list

# print(solution(10))
# # [2, 3, 4, 5, 6, 7, 8, 9, 10]
# =============================================
# # # 시도 7
# # 시도 6에서 0 < n <= 1000이라는 제한사항 고려를 못 함.
# # n = 1 일 경우를 고려해서, range의 start를 n = 2로 하지 않아야 함.
# def solution(n):
#     empty_list=[]
#     for i in range(0, n+1, 2):
#         empty_list.append(i)
#     return empty_list

# # print(solution(9))
# # # [0, 2, 4, 6, 8]
# # print(solution(10))
# # # [0, 2, 4, 6, 8, 10]

# 얼떨결에 리스트 완성
# 더하기만 하면 됨
# =============================================
# 시도 8
def solution(n):
    empty_list=[]
    for i in range(0, n+1, 2):
        empty_list.append(i)
    add_num = 0
    for num in empty_list:
        add_num += num
    return add_num

# print(solution(0))
# # 0
# print(solution(1))
# # 0
# print(solution(2))
# # 2
# print(solution(11))
# # 30