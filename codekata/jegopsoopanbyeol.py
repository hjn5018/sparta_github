# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다.
# 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

# 1 ≤ n ≤ 1,000,000

n = 144
# result = 1
# n = 976
# result = 2

# n = x^2

# sqrt(n) = x

# if sqrt(n) == int or float:
#     return 1
# else:
#     return 2

# ========sqrt못 쓰면?========
# n이 백만까지니까
# x 천까지 range

def solution(n):
    list_ = []
    for i in range(1000):
        i = i * i
        list_.append(i)
    if n in list_:
        return 1
    else:
        return 2

print(solution(144))