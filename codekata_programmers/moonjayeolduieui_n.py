# 문자열 my_string과 정수 n이 매개변수로 주어질 때,
# my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

# my_string은 숫자와 알파벳으로 이루어져 있습니다.
# 1 ≤ my_string의 길이 ≤ 1,000
# 1 ≤ n ≤ my_string의 길이

my_string = "ProgrammerS123"
n = 11

# result = my_string[-1]
# 3

# result = my_string[-1:-3]
# ??
# step에서 -1을 걸지 않았다.

# result = my_string[-1: 3]
# ??
# step에서 -1을 걸지 않았다.

# result = my_string[0:4]
# Prog

# result = my_string[-1:-3:-1]
# 32

# result = my_string[-1:-3:1]
# ??

# result = my_string[0:-3:-1]
# ??
# start 과 stop의 방향이 다르다.

# result = my_string[1:-3:-1]
# ??
# start 과 stop의 방향이 다르다.

result = my_string[-1:-12:-1]
# 321Sremmarg
result = result[::-1]
# grammerS123

print(result)

def solution(my_string, n):
    fliped_string = my_string[-1:-n-1:-1]
    result = fliped_string[::-1]
    return result