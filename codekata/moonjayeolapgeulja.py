# 문자열 my_string과 정수 n이 매개변수로 주어질 때,
# my_string의 앞의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

# my_string은 숫자와 알파벳으로 이루어져 있습니다.
# 1 ≤ my_string의 길이 ≤ 1,000
# 1 ≤ n ≤ my_string의 길이

my_string = "ProgrammerS123"
n = 11
result = "ProgrammerS"
# my_string = "He110W0r1d"
# n = 5
# result = "He110"

# def solution(my_string, n):
#     result = my_string[0:n]
#     print(result)

def solution(my_string, n):
    return my_string[0:n]