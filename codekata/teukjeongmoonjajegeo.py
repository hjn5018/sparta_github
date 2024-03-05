# 문자열 my_string과 문자 letter이 매개변수로 주어집니다.
# my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# 1 ≤ my_string의 길이 ≤ 100
# letter은 길이가 1인 영문자입니다.
# my_string과 letter은 알파벳 대소문자로 이루어져 있습니다.
# 대문자와 소문자를 구분합니다.

# def solution(my_string, letter):
#     if letter in my_string:
#         return my_string - letter
# # TypeError: unsupported operand type(s) for -: 'str' and 'str'
# my_string = "abcdef"
# letter = "f"

# result = solution(my_string, letter)

# print(result)
# ==========================================
# 찾는다
# 슬라이싱한다 -> 그러면 이뉴머레이트 써야함. -> 그러면 리스트??
# -> 그러면 다시 스트링으로 돌려야하는데??
# 합친다



# 아니면 - 해본다 -> 지원하지 않는 타입
# =============================================
def solution(my_string, letter):
    if letter in my_string:
        enumerate(i, my_string)

my_string = "abcdef"
letter = "f"

result = solution(my_string, letter)

print(result)