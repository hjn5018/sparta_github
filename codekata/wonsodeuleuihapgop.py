# 정수가 담긴 리스트 num_list가 주어질 때,
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을
# return하도록 solution 함수를 완성해주세요.

# 2 ≤ num_list의 길이 ≤ 10
# 1 ≤ num_list의 원소 ≤ 9

def solution(num_list):
    mul = 1
    for num in num_list:
        mul *= num
    
    sum = 0
    for num in num_list:
        sum += num
    if mul < sum*sum:
        return 1
    else:
        return 0
