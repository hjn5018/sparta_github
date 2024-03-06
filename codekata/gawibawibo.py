# 가위는 2 바위는 0 보는 5로 표현합니다.
# 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때,
# rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.

# 0 < rsp의 길이 ≤ 100
# rsp와 길이가 같은 문자열을 return 합니다.
# rsp는 숫자 0, 2, 5로 이루어져 있습니다.

# def solution(rsp):
#     answer = ''
#     for case in rsp:
#         if case == '2':
#             answer + '0'
#         elif case == '0':
#             answer + '5'
#         else:
#             answer + '2'
#     return answer
# ====================================================
# rsp = "205"
# # result = "052"
# answer = "여기붙어"
# for case in rsp:
#     # print(case, type(case))
# # 2 <class 'str'>
# # 0 <class 'str'>
# # 5 <class 'str'>
#     if case == "2":
#         answer + "0"
#     elif case == "0":
#         answer + "5"
#         # print("case == '2'")
#         # # case == 2
# # print(answer)
# # # 여기붙어
# # # 붙질 않네??
        
# # print("2"+"1")
# # 21
# # print(""+"122")
# # 122
# # print(answer)
# ========================================================
# 모두  += 하지 않아서 벌어진 일이라..

def solution(rsp):
    answer = ''
    for case in rsp:
        if case == '2':
            answer += '0'
        elif case == '0':
            answer += '5'
        else:
            answer += '2'
    return answer

rsp = "205"

print(solution(rsp))
# 이게 좀........ 직관적이지 않은데................
# 연산하고 자동으로 좀 담아주라..................