# 어떤 세균은 1시간에 두배만큼 증식한다고 합니다.
# 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때
# t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

# 1 ≤ n ≤ 10
# 1 ≤ t ≤ 15

# def solution(n, t):
#     return pow(n, t)
# base는 2여야 함. 2배씩 늘어난다고 함. n은 그냥 곱해지는 디폴트로 ㄱㄱ 
# ==================================
# pow(n, t)

# result = pow(2, 5)
# result = pow(2, 7)

# print(result)
# 32
# 128
# =================================
def solution(n, t):
    return n * pow(2, t)