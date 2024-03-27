def solution(my_string):
#     return *my_string
# SyntaxError: can't use starred expression here
    # 비슷하게 하는 뭐가 있었는데..
    # ------------------------
    # my_list = my_string.split()
    # if my_list[1] == '+':
    #     result = int(my_list[0]) + int(my_list[2])
    # else:
    #     result = int(my_list[0]) - int(my_list[2])
    # return result
    # 연산자는 적어도 하나 포함이므로 여러 개 있을 수 있음
    # ------------------------------
    # return '{}'.format(*my_string)
    # # 3
    # ----------------------------
    # return f'{my_string}'
    # "3 + 4"
    # -------------------------
    # return f'{*my_string}'
    # SyntaxError: can't use starred expression here
    # -----------------------------
    # my_list = my_string.split()
    # return *my_list
    # SyntaxError: can't use starred expression here
    # --------------------------------
    # my_list = my_string.split()
    # return my_list
    # ["3","+","4"]
    # ----------------------
    # my_list = my_string.split()
    # my_string = str(my_list)
    # return my_string
    # "['3', '+', '4']"
    # ------------------------------
    # my_list = my_string.split()
    # my_string = ''
    # for i in my_list:
    #     my_string += i
    # return my_string
    # "3+4"
    # ------------------------------------
    # my_list = my_string.split()
    # my_string = ''
    # for i in my_list:
    #     my_string += i
    # return *my_string
    # SyntaxError: can't use starred expression here
    # --------------------------------
    # my_list = my_string.split()
    # result = int(my_list[0])
    # for i in range(1, len(my_list), 2):
    #     if i == '+':
    #         result += int(my_list[i+1])
    #     else:
    #         result -= int(my_list[i+1])
    # return result
    # 실행한 결괏값 -1이 기댓값 7과 다릅니다.
    # ------------------------------------
    my_list = my_string.split()
    result = int(my_list[0])
    for i in range(1, len(my_list), 2):
        if my_list[i] == '+':
            result += int(my_list[i+1])
        if my_list[i] == '-':
            result -= int(my_list[i+1])
    return result

# --------------------------------------------------------
# solution = eval
# solution = eval
# solution = eval
# solution = eval
