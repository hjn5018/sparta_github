# list_ = [1, 2, 3, 4]

# result = list_[:0]
# print(result)
# #[]

# result = list_[1:]
# print(result)
# # [2, 3, 4]

# result = list_[:0] + list_[1:]
# print(result)
# # [2, 3, 4]
# =================================
# def solution(numbers):
#     max = 0
#     for i in range(len(numbers)):
#         numbers_except_i = numbers[:i] + numbers[i + 1:]
#         for j in range(len(numbers_except_i)):
#             if max < numbers[i] * numbers_except_i[j]:
#                 max = numbers[i] * numbers_except_i[j]
#     return max
# 7번 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
# 가장 큰 숫자 두 개를 곱하는 경우도 있지만
# 숫자의 범위가 자연수가 아닌 -10,000 ≤ numbers의 원소 ≤ 10,000 이기 때문에 가장 작은 숫자 두 개를 곱한 것이 답일 수 있습니다.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# =======================================
def solution(numbers):
    max = numbers[0] * numbers[1]
    for i in range(len(numbers)):
        numbers_except_i = numbers[:i] + numbers[i + 1:]
        for j in range(len(numbers_except_i)):
            if max < numbers[i] * numbers_except_i[j]:
                max = numbers[i] * numbers_except_i[j]
    return max
