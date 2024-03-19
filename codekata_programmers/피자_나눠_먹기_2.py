# 처음 생각은 n명만큼 0000000놓고 처음과 마지막이 같은 수라면 공평하게 나눠진 것
# 하지만 구현하기 힘들었다.
# def solution(n):
#     list_ = [0] * n
#     k = 0
#     for i in range(50):
#         for j in range(6):
#             k = (i * 6) + j
#             list_[k] += 1
#         if list_[0] == list_[n-1]:
#             return i+1
# =================================
# n = 10

# list_ = [0] * n
# k = 0
# for i in range(50):
#     for j in range(6):
#         k = (i * 6) + j
#         list_[k] += 1
#         # IndexError: list index out of range
#     if list_[0] == list_[n-1]:
#         print(i+1)
# ==========================================
def solution(n):
#     n과 6의 최소공배수를 구한다 -> x
#     n을 x로 나눈 값이 result이다.
#     2,3,6으로 나누었을 때 나누어진다면 최소공배수가 2,3,6이다.
#     6부터 if들어간다
#     3
#     2
#     안되면
#     n이 result이다.
    if n % 6 == 0:
        return n // 6
    elif n % 3 == 0:
        return n // 3
    elif n % 2 == 0:
        return n // 2
    else:
        return n