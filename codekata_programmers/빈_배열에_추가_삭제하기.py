# def solution(arr, flag):
#     answer = []
#     for i in range(len(flag)):
#         if flag[i]:
#             answer.append(arr[i]) * arr[i] * 2
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
#         else:
#             del answer[len(answer)-arr[i]:]
#     return answer
# ===========================================
def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i]:
            answer += [arr[i]] * arr[i] * 2
        else:
            del answer[len(answer)-arr[i]:]
    return answer
