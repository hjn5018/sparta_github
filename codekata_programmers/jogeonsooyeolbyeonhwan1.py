# 정수 배열 arr가 주어집니다.
# arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고,
# 50보다 작은 홀수라면 2를 곱합니다.
# 그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.

# 1 ≤ arr의 길이 ≤ 1,000,000
# 1 ≤ arr의 원소의 값 ≤ 100

# def solution(arr):
#     for num in arr:
#         if num >= 50:
#             num /= 2
#         else:
#             num *= 2
#     return arr

# arr = [1, 2, 3, 100, 99, 98]

# result = solution(arr)

# print(result)
# [1, 2, 3, 100, 99, 98]

# 원소마다 적용된 게 휘발된건가..?
# ======================================================

# arr = [1, 2, 3, 100, 99, 98]

# for i in arr:
#     i /= 2

# print(arr)
# [1, 2, 3, 100, 99, 98]
# 직접 넣을 수가 없다??

# for i in arr:
#     i /= 2
#     print(i)
# 0.5
# 1.0
# 1.5
# 50.0
# 49.5
# 49.0
# 실행을 하긴 하는데..

# for i in arr:
#     i = i / 2

# print(arr)
# [1, 2, 3, 100, 99, 98]
# 표현이 문제인 건 아닌 것 같기도 하고..

# for i in arr:
#     arr.remove(i)

# print(arr)
# [2, 100, 98]
#???????? [2, 100, 98]는 왜 나오지
# 일단 없어진건 1, 3, 99
# ===============================================
# for i in arr:
#     arr.remove(i)
#     print(arr)

# # 1 없어지고, 3 없어지고, 99 없어졌는데..

# 1. 값이 i인 요소를 지운다.
# 2. index가 i인 요소를 지운다.

# 내가 생각한 것은??
# i번째가 돌면서 i번째를 다 지우는 것

# 하지만 for i in arr:는
# range가 아니다!!

# 즉, i는 index가 아니고 요소이다!!

# 그렇다면
# def solution(arr):
#     for num in arr:
#         if num >= 50:
#             num /= 2
#         else:
#             num *= 2
#     return arr
# 이게 작동하지 않는 이유는??? arr에 저장하지 않아서 인 것 같은데

# arr.append(num/2)를 하면
# 남아있는 num은 지워야하는데...
# remove는 index가 아닌 특정 값을 지울까??

# list_ = [2,2,2,2]
# [2, 2, 2]
# 2를 다 지우진 않네

# list_ = [1,2,3,4]
# [1, 3, 4]

# list_ = [1, 9, 1, 2, 3, 4]
# # [1, 9, 1, 3, 4]
# # 값을 콕 집어서 버리긴 하네
# list_.remove(2)
# print(list_)


# list_ = [1, 9, 1, 2, 3, 4]
# list_.remove()
# print(list_)
# TypeError: remove() takes exactly one argument (0 given)
# 값을 쥐어주긴 해야하네..
# 그렇다치고.. 인덱스로 지우는건...?
# ===============================================
def solution(arr):
    new_arr = []
    
    for num in arr:
        if num >= 50 and num % 2 == 0:
            num /= 2
            new_arr.append(num)
        elif num < 50 and num % 2 == 1:
            num *= 2
            new_arr.append(num)
        else:
            new_arr.append(num)
            
    return new_arr

# 솔직히 어레이 하나 더 생성해서 넣는 거 짜친다.