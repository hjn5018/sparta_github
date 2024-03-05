# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

# -10,000 ≤ numbers의 원소 ≤ 10,000
# 1 ≤ numbers의 길이 ≤ 1,000
# ===============================================
# def solution(numbers):
#     for num in numbers:
#         num == num * 2
#     return numbers

# numbers = [1,2,3,4,5]

# result = solution(numbers)

# print(result)
# # [1, 2, 3, 4, 5]
# # ???????????????
# ===============================================
# numbers = [1,2,3,4,5]

# for num in numbers:
#     num = 2*num
# print(numbers)
# ===============================================
def solution(numbers):
    tw_list = []
    for num in numbers:
        tw_list.append(num * 2)
    return tw_list

numbers = [1,2,3,4,5]

result = solution(numbers)

print(result)
# [2, 4, 6, 8, 10]
# ????????????????????????????????????