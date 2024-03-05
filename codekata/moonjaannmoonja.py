str1 = "ab6CDE443fgh22iJKlmn1o"
str2 = "6CD"

# if str2 in str1:
#     print("있다.")
# 있다.


# if str1 in str2:
#     print("있다.")
# else:
#     print("없다.")
# # 없다.

# 문자열 str1, str2가 매개변수로 주어집니다.
# str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

# 1 ≤ str1의 길이 ≤ 100
# 1 ≤ str2의 길이 ≤ 100
# 문자열은 알파벳 대문자, 소문자, 숫자로 구성되어 있습니다.

def solution(str1, str2):
    # if str2 in str1:
    #     return 1
    # else:
    #     return 2
result = solution(str1, str2)

print(result)