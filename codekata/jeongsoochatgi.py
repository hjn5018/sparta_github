# 정수 리스트 num_list와 찾으려는 정수 n이 주어질 때,
# num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.

# 3 ≤ num_list의 길이 ≤ 100
# 1 ≤ num_list의 원소 ≤ 100
# 1 ≤ n ≤ 100

# def solution(num_list, n):
#     if str(n) in num_list:
#         return 1
#     else:
#         return 0

# 입력값 〉	[1, 2, 3, 4, 5], 3
# 기댓값 〉	1
# 실행 결과 〉	실행한 결괏값 0이 기댓값 1과 다릅니다.

# <str> in으로 조사하려고 했다.
# 틀린 걸 보니
# num_list의 요소가 int인 것 같다.
# ===========================================

# def solution(num_list, n):
#     for num in num_list:
#         if num == n:
#             return 1
#         else:
#             return 0
# 입력값 〉	[1, 2, 3, 4, 5], 3
# 기댓값 〉	1
# 실행 결과 〉	실행한 결괏값 0이 기댓값 1과 다릅니다.
# ==================================================
# def solution(num_list, n):


num_list = [1,2,3,4,5]
# result = type(num_list)
# # <class 'list'>
# result = type(num_list[1])
# # <class 'int'>
# # print(result)

def solution(num_list, n):
    result = 0
    for num in num_list:
        if num == n:
            result += 1
    if result > 0:
        return 1
    else:
        return 0

# # for문으로 뽑기 좀 힘든데..?


# for num in num_list:
#     num = str(num)

# num_list = ['1']

# print(num_list)
# # ['1']
# # print(type(num_list[1]))

