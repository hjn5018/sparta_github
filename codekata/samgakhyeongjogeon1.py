# 삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다.
# 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.

# sides의 원소는 자연수입니다.
# sides의 길이는 3입니다.
# 1 ≤ sides의 원소 ≤ 1,000

# sides = [1, 2, 3]
# sides = [199, 72, 222]


def solution(sides):
    sorted_sides = sorted(sides)
    if sorted_sides[2] < sorted_sides[1] + sorted_sides[0]:
        return 1
    else:
        return 2


print(solution([199, 72, 222]))
# TypeError: 'function' object is not subscriptable