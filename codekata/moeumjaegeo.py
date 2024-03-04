# 문자열 my_string이 매개변수로 주어질 때
# 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# my_string은 소문자와 공백으로 이루어져 있습니다.
# 1 ≤ my_string의 길이 ≤ 1,000
# ============================================
# def solution(my_string):
#     answer = ''
#     return answer
# ============================================
# my_string = "bus"
# my_string = "nice to meet you"
# =============================================
# my_string = "bus"

# result = my_string[0]
# # b
# result = my_string[1]
# # u
# # print(result)

# 1. 문자열의 인덱스마다 aeiou를 찾는다.
# 2. 없앤다.
# 3. while aeiou 없을 때까지 aeiou 찾는다.
# 4. 다 없앴으면 return my_string 반환한다.

# my_string = "bus"

# # my_string -+ "u"
# # # TypeError: bad operand type for unary +: 'str'

# my_string
# print(my_string)

# 없앤다의 기능을 떠올리기 힘들다.

# python documentation
# translate method
# s = 'abc12321cba'
# print(s)
# print(s.translate({ord(i): None for i in 'abc'}))

# my_string = "bus"
# # print(my_string.translate({ord(i): None for i in 'aeiou'}))
# result = my_string.translate({ord(i): None for i in 'aeiou'})
# print(result)
# # .translate() method는 str을 반환한다.

# =====================================================
# 함수와 method의 반환 차이

# # none을 반환하지만 정렬해주는 sort() method
# l = [5,7,3,1,9]
# print(l.sort())
# # None
# print(l)
# # [1, 3, 5, 7, 9]

# # list를 반환해주지만 원래 리스트는 그대로 두는 함수.
# l = [5,7,3,1,9]
# print(sorted(l))
# # [1, 3, 5, 7, 9]

# result = sorted(l)
# print(result)
# # [1, 3, 5, 7, 9]

# print(l)
# # [5, 7, 3, 1, 9]
# ========================================================
def solution(my_string):
    return my_string.translate({ord(i): None for i in 'aeiou'})

# my_string = "bus"
# # bs
# my_string = "nice to meet you"
# # nc t mt y
# result = solution(my_string)
# print(result)
