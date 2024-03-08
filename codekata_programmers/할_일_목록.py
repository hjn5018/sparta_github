# def solution(todo_list, finished):
#     list_ = []
#     for i in range(len(finished)):
#         if finished[i] == 'false':
#             list_.append(todo_list[i])
#     return list_
# # 실행한 결괏값 []이 기댓값 ["practiceguitar","studygraph"]과 다릅니다.
# =======================================================
# def solution(todo_list, finished):
#     list_ = []
#     for i in range(len(finished)):
#         if finished[i] == false:
#             list_.append(todo_list[i])
#     return list_
# # NameError: name 'false' is not defined
# ==========================================================
# todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
# finished = [true, false, true, false]
# # result = ["practiceguitar", "studygraph"]

# print(todo_list)
# NameError: name 'true' is not defined
# ?????????????????????????????????????????????????????
# =========================================================
# todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
# print(todo_list)
# ['problemsolving', 'practiceguitar', 'swim', 'studygraph']

# result = 1 == True
# print(result)
# True

# result = 1 == true
# print(result)
# NameError: name 'true' is not defined

# result = 1 == 'true'
# print(result)
# False

# result = 1 == 'True'
# print(result)
# False
# =======================================================
# def solution(todo_list, finished):
#     list_ = []
#     for i in range(len(finished)):
#         if finished[i] == 'false':
#             list_.append(todo_list[i])
#     return list_

# todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
# finished = [true, false, true, false]
# result = ["practiceguitar", "studygraph"]

# 여기서 우선 true라는 값이 아무런 타입이 아닌 거 아닌가.......
# ===========================================================
def solution(todo_list, finished):
    list_ = []
    for i in range(len(finished)):
        if finished[i] == False :
            list_.append(todo_list[i])
    return list_
# 장난하나.......