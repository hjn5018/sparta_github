# def solution(my_string, s, e):
#     result = ''
#     for i in my_string:
#         if s <= i <= e:
#             result += my_string[i-s+e]
#         else:
#             result += my_string[i]
#     return result
# ======================================
my_string = "Progra21Sremm3"
s = 6
e = 12
result = "ProgrammerS123"


result = ''
for i in range(len(my_string)):
    if s <= i <= e:
        result += my_string[e-i+s]
    else:
        result += my_string[i]
print(result)

