# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때,
# array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

# 1 ≤ array의 길이 ≤ 100
# 0 ≤ array의 원소 ≤ 1,000
# 0 ≤ n ≤ 1,000

def solution(array, n):
    i = 0
    for j in array:
        if n == j:
            i += 1
    return i

result = solution([1, 1, 2, 3, 4, 5], 2)


print(result)

# list_ = [1, 1, 2, 3, 4, 5]
