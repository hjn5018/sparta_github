# 문자열 my_string이 매개변수로 주어집니다.
# my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# 1 ≤ my_string의 길이 ≤ 1,000
# my_string은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.

# my_string = "aAb1B2cC34oOp"
# result = 10

# for i in my_string:
#     if i in [1,2,3,4,5,6,7,8,9]:
#         print(i)

# for i in my_string:
#     [1,2,3,4,5,6,7,8,9] in i
#     print(f"i, {i}")
# # TypeError: 'in <string>' requires string as left operand, not list

# if my_string in [1,2,3,4,5,6,7,8,9]:
#     print("응")
# else:
#     print("아니야")
# # 아니야

# if my_string in 123456789:
#     print("응")
# else:
#     print("아니야")
# # TypeError: argument of type 'int' is not iterable

# if my_string in 1:
#     print("응")
# else:
#     print("아니야")
# # TypeError: argument of type 'int' is not iterable

# if my_string in "123456789":
#     print("응")
# else:
#     print("아니야")
# # 아니야

# if my_string in [123456789]:
#     print("응")
# else:
#     print("아니야")
# # 아니야
# =============================
# list_ = []
# for i in my_string:
#     for j in [1,2,3,4,5,6,7,8,9]:
#         if "j" in my_string:
#             list_.append(j)
# # print(list_)
# # []
# ================================
# for i in [1,2,3,4,5,6,7,8,9]:
#     print(type(i))
# # <class 'int'>
# # <class 'int'>
# # <class 'int'>
# # <class 'int'>
# # <class 'int'>
# # <class 'int'>
# # <class 'int'>
# # <class 'int'>
# # <class 'int'>
            
# list_ = []
# for i in my_string:
#     for j in [1,2,3,4,5,6,7,8,9]:
#         if "j" == i:
#             list_.append(j)
# # print(list_)
# # # []

# result = my_string in "a"
# # False
# result = "a" in my_string
# # True
# result = "1" in my_string
# # True

# print(result)

# for i in range(1, 11):
#     print(type(i))
# <class 'int'>
# <class 'int'>
# <class 'int'>
# <class 'int'>
# <class 'int'>
# <class 'int'>
# <class 'int'>
# <class 'int'>
# <class 'int'>
# <class 'int'>

# for i in range(1, 11):
#     result = "i" in my_string
#     print(result)

# False
# False
# False
# False
# False
# False
# False
# False
# False
# False

# for i in range(1, 11):
#     print("i")
# i
# i
# i
# i
# i
# i
# i
# i
# i
# i

# for i in [1,2,3,4,5,6,7,8,9]:
#     print(i, type(i), "i", type("i"), str(i))

# for i in range(1, 11):
#     print(str(i))

# 찾았다 원피스
# =========================================
# # my_string = "aAb1B2cC34oOp"
# # [1, 2, 3, 4]
# # my_string = "1a2b3c4d123"
# # [1, 2, 3, 4, 1, 2, 3]

# list_ = []
# for i in my_string:
#     for j in range(1, 11):
#         if i == str(j):
#             list_.append(j)
# print(list_)
# ===========================================
# # my_string = "aAb1B2cC34oOp"
# # 10
# # my_string = "1a2b3c4d123"
# # 16
# sum = 0
# for i in my_string:
#     for j in range(1, 11):
#         if i == str(j):
#             sum += j

# print(sum)

def solution(my_string):
    sum = 0
    for i in my_string:
        for j in range(1, 11):
            if i == str(j):
                sum += j
    return sum