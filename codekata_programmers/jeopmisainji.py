# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

# 1 ≤ my_string의 길이 ≤ 100
# 1 ≤ is_suffix의 길이 ≤ 100
# my_string과 is_suffix는 영소문자로만 이루어져 있습니다.
# =======================================================
def solution(my_string, is_suffix):
    len_is_suffix = len(is_suffix)
    # return len_is_suffix
    # 3
    # a = my_string[:-4:-1]
    # return a
    # b = is_suffix[::-1]
    # return b
    # ana
    if my_string[:-len_is_suffix-1:-1] == is_suffix[::-1]:
        return 1
    else:
        return 0

my_string = "banana"
is_suffix = "ana"

result = solution(my_string, is_suffix)

print(result)
# ============================================

my_string = "banana"
result = my_string[-1:]
# a
result = my_string[-1::]
# a
result = my_string[:]
# banana
result = my_string[-1:-2]
# ???
result = my_string[-1:2]
# ???
result = my_string[1:2]
# a
result = my_string[0:2]
# ba
result = my_string[:2]
# ba
result = my_string[-1:-3]
# ???
result = my_string[::-1]
# ananab
result = my_string[-1::-1]
# ananab
result = my_string[-1:-3:-1]
# an
result = my_string[-1:-4:-1]
# ana
result = my_string[-1:-4]
# ???
result = my_string[::2]
# bnn
result = my_string[:-1:-1]
# ???
result = my_string[:-2:-1]
# a
result = my_string[:-3:-1]
# an
result = my_string[-1]
# a
result = my_string[-2]
# n
result = my_string[-6]
# b
# result = my_string[6]
# IndexError: string index out of range
# result = my_string[-7]
# IndexError: string index out of range
result = my_string[:-3:-2]
# a
my_string = "가나다라마바사"
result = my_string[:-3:-2]
# 사
result = my_string[:-3:-3]
# 사
result = my_string[:-3:-1]
# 사바
result = my_string[:-6:-2]
# 사마다
result = my_string[-2:-6:-2]
# 바라
# print(result)

# 0  1  2  3  4  5
# b  a  n  a  n  a 
# -6 -5 -4 -3 -2 -1


# 1   2   3   4   5   6   7
# 가  나  다  라  마  바  사
# -7  -6  -5  -4  -3  -2  -1