# 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때,
# 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

# 1 ≤ array의 길이 ≤ 100
# 1 ≤ height ≤ 200
# 1 ≤ array의 원소 ≤ 200

def solution(array, height):
    i = 0
    for chingoo_ki in array:
        if chingoo_ki > height:
            i += 1
    return i





# array = [149, 180, 192, 170]
# height = 167
# result = 3