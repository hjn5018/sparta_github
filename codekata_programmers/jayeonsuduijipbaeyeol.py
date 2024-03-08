# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# n은 10,000,000,000이하인 자연수입니다.

# def solution(n):
#     list_ = []
#     for i in n:
#         print()

# print(solution(542))

# ==================================================
# n = 12345
# list_ = []
# for i in n:
# #     print(i)
# # # TypeError: 'int' object is not iterable
# ==================================================
    
# n = 12345
# list_ = []
# print(list(n))
# # TypeError: 'int' object is not iterable
# ======================================================
# n = 12345
# list_ = []
# n = str(n)
# # print(type(n))
# # # <class 'str'>
# for i in n:
#     list_.append(i)
# # print(list_)
# # # ['1', '2', '3', '4', '5']
# ==========================================================
# n = 12345
# list_ = []
# n = str(n)

# for i in n:
#     list_.append(i)
# print(list_)
# # ['1', '2', '3', '4', '5']
# list_[::-1]
# print(list_)
# # ['1', '2', '3', '4', '5']
# # ???????????????????????????????????????????????????/
# ====================================================================
# n = 12345
# list_ = []
# n = str(n)

# for i in n:
#     list_.append(i)
# #     print(list_[int(i)-1])
# # # 1
# # # 2
# # # 3
# # # 4
# # # 5
# ============================================================
# n = 12345
# list_ = []
# n = str(n)

# for i in n:
#     list_.append(int(i))
# # print(list_)
# # # [1, 2, 3, 4, 5]
# ======================================================
# n = 12345
# list_ = []
# n = str(n)

# for i in n:
#     list_.append(int(i))
# print(list_[::-1])

def solution(n):
    list_ = []
    n = str(n)

    for i in n:
        list_.append(int(i))
    return list_