# 두 배열이 얼마나 유사한지 확인해보려고 합니다.
# 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

# 1 ≤ s1, s2의 길이 ≤ 100
# 1 ≤ s1, s2의 원소의 길이 ≤ 10
# s1과 s2의 원소는 알파벳 소문자로만 이루어져 있습니다
# s1과 s2는 각각 중복된 원소를 갖지 않습니다.

# def solution(s1, s2):
    

# s1 = ["a", "b", "c"]
# s2 = ["com", "b", "d", "p", "c"]
# result = 2
# # 2

# s1 = ["n", "omg"]
# s2 = ["m", "dot"]
# result = 0
# # 0

# count = 0
# for s1_element in s1:
#     for s2_element in s2:
#         if s1_element == s2_element:
#             count += 1

# print(count)
# ===================================
def solution(s1, s2):
    count = 0
    for s1_element in s1:
        for s2_element in s2:
            if s1_element == s2_element:
                count += 1
    return count
