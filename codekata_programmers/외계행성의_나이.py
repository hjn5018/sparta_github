# def solution(age):
#     num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     str_ = 'abcdefghij'
#     str_ = str_.split()
#     dict(zip(num, str_))
    
#     result = ''
#     for i in age:
#         result += dict[i]
    
#     return result
# ==========================================

# age = 23

# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# str_ = 'abcdefghij'
# str_ = str_.split()
# dict_ = dict(zip(num, str_))

# result = ''

# age = str(age).split()
# print(age)
# ['23']

# for i in str(age).split():
#     print(i)
    # i = int(i)
    # result += dict[i]

# print(dict_)
# {0: 'abcdefghij'}
# print(str_)
# ['abcdefghij']
# ================================================
age = 23

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
str_ = 'abcdefghij'
str_list = []
for i in str_:
    str_list.append(i)
# print(str_list)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
dict_ = dict(zip(num, str_list))

age_list = []
for i in str(age):
    age_list.append(int(i))
# print(age_list)
# [2, 3]

result = ''
for i in age_list:
    result += dict_[i]

print(result)
# =======================================================
def solution(age):
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    str_ = 'abcdefghij'
    str_list = []
    for i in str_:
        str_list.append(i)
    
    dict_ = dict(zip(num, str_list))
    
    age_list = []
    for i in str(age):
        age_list.append(int(i))

    result = ''
    for i in age_list:
        result += dict_[i]

    return result 