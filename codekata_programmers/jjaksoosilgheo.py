# 정수 n이 매개변수로 주어질 때,
# n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

# 1 ≤ n ≤ 100

n = 10
def solution(n):
    list_ = []
    for i in range(n):
        i += 1
        if i % 2 == 1:
            list_.append(i)
    return list_

print(list_)