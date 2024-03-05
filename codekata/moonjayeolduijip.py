# 문자열 my_string이 매개변수로 주어집니다.
# my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

# 1 ≤ my_string의 길이 ≤ 1,000

# def solution(my_string):
    




# 1. 원소 간 뒤집
# my_string[i], my_string[i+1] = my_string[i+1], my_string[i]

# 2. 하려면 for문?
# def solution(my_string):
#     for 

# 3. 하려면 len(my_string)?
# my_string = "jaron"

# print(len(my_string))
# 5

# =======================
# def solution(my_string):
#     n = len(my_string)
#     for i in range(n-1):
#         my_string[i], my_string[i+1] = my_string[i+1], my_string[i]
#     return my_string

# result = solution("jaron")

# print(result)
# # TypeError: 'str' object does not support item assignment
# ==============================
# ??????????????????????????/
# 그렇다면 리스트로 변환해서.......
# =================================
# def solution(my_string):
#     ms_list = []
#     for i in my_string:
#         ms_list.append(i)
#     # return ms_list
#     # # ['j', 'a', 'r', 'o', 'n']
    
#     n = len(my_string)

#     for i in range(n-1):
#         ms_list[i], ms_list[i+1] = ms_list[i+1], ms_list[i]
#     return ms_list

# result = solution("jaron")

# print(result)
# ==============================================
# 그렇다면 리스트 원소들을 다시 스트링으로 변환하려면?????
# str(list)????
# 안되네..

def solution(my_string):
    ms_list = []
    for i in my_string:
        ms_list.append(i)
    # return ms_list
    # # ['j', 'a', 'r', 'o', 'n']
    
    n = len(my_string)

    for i in range(n-1):
        ms_list[i], ms_list[i+1] = ms_list[i+1], ms_list[i]
    # return str(ms_list)
    # # ['a', 'r', 'o', 'n', 'j']

result = solution("jaron")

print(result)