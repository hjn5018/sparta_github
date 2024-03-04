# 다음과 같이 숫자로 이루어진 배열이 있을때, 이 배열 내에서 가장 큰 수를 반환하시오.
# [3, 5, 6, 1, 2, 4]


random_list = [3, 5, 6, 1, 2, 4]


def find_max_num(list):
    max = 0
    for num in list:
        if num > max:
            max = num
    return max

result = find_max_num(random_list)

print(result)