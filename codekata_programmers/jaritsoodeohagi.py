# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# N의 범위 : 100,000,000 이하의 자연수

def solution(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

print(solution(648))