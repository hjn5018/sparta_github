# 정수가 담긴 리스트 num_list가 주어집니다.
# num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록
# solution 함수를 완성해주세요.

# 2 ≤ num_list의 길이 ≤ 10
# 1 ≤ num_list의 원소 ≤ 9
# num_list에는 적어도 한 개씩의 짝수와 홀수가 있습니다.

def solution(num_list):
    odd_string = ""
    even_string = ""
    for num in num_list:
        if num % 2 == 0:
            even_string += str(num)
        else:
            odd_string += str(num)
    return int(even_string) + int(odd_string)

# 처음에는 스트링이 아니라 리스트로 했는데, 또 for문 돌리기 좀 그랬음.