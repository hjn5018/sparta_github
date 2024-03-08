# 문자열 my_string과 정수 k가 주어질 때,
# my_string을 k번 반복한 문자열을 return
# 하는 solution 함수를 작성해 주세요.

# 1 ≤ my_string의 길이 ≤ 100
# my_string은 영소문자로만 이루어져 있습니다.
# 1 ≤ k ≤ 100

def solution(my_string, k):
    new_string = ""
    # new_string = new_string + (my_string * k)
    new_string += (my_string * k)
    return new_string


my_string = "string"
k = 3
my_string = "love"
k = 10

new_string = ""

new_string = new_string + my_string*k

print(new_string)