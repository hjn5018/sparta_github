# 이 문제에서 두 정수 배열의 대소관계를 다음과 같이 정의합니다.

# 두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
# 배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여 다르다면 더 큰 쪽이 크고, 같다면 같습니다.
# 두 정수 배열 arr1과 arr2가 주어질 때, 위에서 정의한 배열의 대소관계에 대하여 arr2가 크다면 -1, arr1이 크다면 1, 두 배열이 같다면 0을 return 하는 solution 함수를 작성해 주세요.

# 1 ≤ arr1의 길이 ≤ 100
# 1 ≤ arr2의 길이 ≤ 100
# 1 ≤ arr1의 원소 ≤ 100
# 1 ≤ arr2의 원소 ≤ 100
# 문제에서 정의한 배열의 대소관계가 일반적인 프로그래밍 언어에서 정의된 배열의 대소관계와 다를 수 있는 점에 유의해주세요.

def solution(arr1, arr2):
    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1
    else:
        sum_arr1 = 0
        sum_arr2 = 0
        for i in arr1:
            sum_arr1 += i
        for j in arr2:
            sum_arr2 += j
        if sum_arr1 > sum_arr2:
            return 1
        elif sum_arr1 < sum_arr2:
            return -1
        else:
            return 0