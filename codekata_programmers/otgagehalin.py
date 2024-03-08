# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

# 10 ≤ price ≤ 1,000,000
# price는 10원 단위로(1의 자리가 0) 주어집니다.
# 소수점 이하를 버린 정수를 return합니다.

# def solution(price):
#     if price > 500000:
#         reduce = 0.2
#     elif price > 300000:
#         reduce = 0.1
#     elif price > 100000:
#         reduce = 0.05
#     price = price * (1 - reduce)
#     return price
# # 런타임 에러 ^o^
# ==============================================
# price = 150000	

# if price > 500000:
#     reduce = 0.2
# elif price > 300000:
#     reduce = 0.1
# elif price > 100000:
#     reduce = 0.05
# price = price * (1 - reduce)
# # price *= (1 - reduce)
# print(price)
# ===============================================
# def solution(price):
#     price = price * (1 - reduce)
#     if price > 500000:
#         reduce = 0.2
#     elif price > 300000:
#         reduce = 0.1
#     elif price > 100000:
#         reduce = 0.05
#     return price
# # UnboundLocalError: local variable 'reduce' referenced before assignment
# ============================================
# list_ = [100000, 300000, 500000]
# dict_ = {100000:0.05, 300000:0.1, 500000:0.2}
# print(dict_[0])
# # KeyError: 0

# print(dict_[list[0]])
# # TypeError: 'type' object is not subscriptable

# for price in list_:
#     print(dict_[price])
# # 0.05
# # 0.1
# # 0.2

# price = 150000

# if price > 500000:
#     reduce = 0.2
# elif price > 300000:
#     reduce = 0.1
# elif price > 100000:
#     reduce = 0.05
# price = price * (1 - reduce)

# print(price)
# ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ

def solution(price):
    if price >= 500000:
        reduce = 0.2
    elif price >= 300000:
        reduce = 0.1
    elif price >= 100000:
        reduce = 0.05
    else:
        reduce = 0
    price = price * (1 - reduce)
    price = int(price)
    return price
# # =======한별님 코드===========
# def solution(price):
#     if price >= 500000:
#         answer = price * .80
#     elif price >= 300000:
#         answer = price* .90
#     elif price >= 100000:
#         answer = price* .95
#     else:
#         answer = price
#     return int(answer)
# # =============준성님 코드=========
# import math
# def solution(price):
#     answer = 0
#     if 100000 <= price < 300000:
#         answer = math.floor(price * 0.95)
#     elif 300000 <= price < 500000:
#         answer = math.floor(price * 0.9)
#     elif price >= 500000:
#         answer = math.floor(price * 0.8)
#     else:
#         answer = price #실수 조심
#     return answer

