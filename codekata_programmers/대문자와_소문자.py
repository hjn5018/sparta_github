def solution(my_string):
    copy_my_string = my_string
    my_string = my_string.lower()

    for letter in my_string:
        for letter_c in copy_my_string:
            if letter_c == letter:
                letter_c = letter_c.upper()
    return copy_my_string
# 입력값 그대로 뱉어버림
# =================================================
def solution(my_string):
    lower_my_string = my_string.lower()
    
    for i in range(len(my_string)):
        if my_string[i] == lower_my_string[i]:
            lower_my_string[i] = lower_my_string[i].upper()
    return lower_my_string
# TypeError: 'str' object does not support item assignment
# =====================================================
def solution(my_string):
    empty_string = ""
    for i in my_string:
        if i == i.upper():
            empty_string += i.lower()
        else:
            empty_string += i.upper()
    return empty_string
# 통과 ^^
# 근데 assignment라는게 ........... 좀 모호하긴하네........
# 이미 있는 값에 다른 값을 넣는 게 안되고
# 그니까 ==는 안되고 +=는 되는데,
# ==는 assignment고 +=는 append인 개념인가..
# find가 in인 개념인가????