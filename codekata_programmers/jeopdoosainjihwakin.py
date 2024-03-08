# 어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
# 문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

# 1 ≤ my_string의 길이 ≤ 100
# 1 ≤ is_prefix의 길이 ≤ 100
# my_string과 is_prefix는 영소문자로만 이루어져 있습니다.

# def solution(my_string, is_prefix):
#     len_is_prefix = len(is_prefix)
#     if is_prefix == my_string[:len_is_prefix-1]:
#         return 1
#     else:
#         return 0
    
    # if is_prefix in my_string의 n번째까지
    # ->
    # is_prefix의 길이 재고
    # my_string n번째까지가 같은지 확인
    
# 입력값 〉	"banana", "ban"
# 기댓값 〉	1
# 실행 결과 〉	실행한 결괏값 0이 기댓값 1과 다릅니다.
# =====================================================
# def solution(my_string, is_prefix):
#     len_is_prefix = len(is_prefix)
#     # return len_is_prefix
#     return my_string[:len_is_prefix-1]
#     # ba
#     if is_prefix == my_string[:len_is_prefix-1]:
#         return 1
#     else:
#         return 0
    

# my_string = "banana"

# is_prefix = "ban"

# result = solution(my_string, is_prefix)

# print(result)
# =======================================================
def solution(my_string, is_prefix):
    len_is_prefix = len(is_prefix)
    if is_prefix == my_string[:len_is_prefix]:
        return 1
    else:
        return 0