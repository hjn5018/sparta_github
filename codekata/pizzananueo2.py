# 머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다.
# 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때,
# n명의 사람이 최소 한 조각 이상 피자를 먹으려면
# 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

# 2 ≤ slice ≤ 10
# 1 ≤ n ≤ 100

def solution(slice, n):
    if n % slice == 0:
        return n / slice
    else:
        return int(n / slice) + 1

# slice = 4
# n = 12
# # result = 2
# # slice * result / n >= 1
# # ->
# # slice * result >= n
# # ->
# # result >= n / slice
# # ->
# # result = int(n/slice) + 1 (n/slice가 1.xxx인 경우)
# # result = n/slice (n/slice가 정수인 경우)

# # 그러면,
# # n // slice가 int로 나오면 n/slice하고
# # else로 int(n/slice) + 1빼기?

# if n // slice == int:
#     result = n/slice
# else:
#     result = int(n/slice) + 1

# print(result)
# # 4??????????????
# print(n // slice)
# # 3
# print(type(n // slice))
# # <class 'int'>

# print(n/slice)
# # 3.0
# ================================================================

# slice = 7
# n = 10


# if type(n / slice) == int:
#     result = n / slice
# elif n // slice != int:
#     result = int(n / slice) + 1

# print(result)