# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다.
# 피자를 나눠먹을 사람의 수 n이 주어질 때,
# 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

# 1 ≤ n ≤ 100

# def solution(n):
    
# =====================================
# if type(n / 7) == type(1.2):
#     n +1
# elif type(n / 7) == type(2):
#     n
# =====================================
# n = 7
# print(int(n/7))
# # 1

# n = 15
# print(int(n/7))
# # 2


# print((n/7).__floor__())

# print(type(n / 7))
# # <class 'float'>

# print(type(1.3) == float)
# True
# =========================================
# def solution(n):
#     if type(n / 7) == float:
#         return int(n // 7) + 1
#     elif type(n / 7) == int:
#         return n / 7
    
# # 하.. 나누면 다 float이네;;
# =========================================
# def solution(n):
#     if type(n / 7) == float:
#         return int(n // 7) + 1
#     elif n % 7 == 0:
#         return n / 7
# 순서도 바꿔야겠다.
# =========================================
def solution(n):
    if n % 7 == 0:
        return n / 7
    elif type(n / 7) == float:
        return n // 7 + 1