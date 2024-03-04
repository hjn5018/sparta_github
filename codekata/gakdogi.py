# 내 최종 답안
def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4
# =========================================
# def solution(angle):
#     answer = 0
#     return answer

# print(answer)
# print(solution(1))
# # 0
# =======================================

# def solution(angle):
#     if 0 < angle < 90:
#         return 1

# print(solution(55))
# # 1
# # 예각 테스트 통과
# =========================================
# def solution(angle):
#     if 0 < angle < 90:
#         return 1
#     elif angle == 90:
#         return 2
#     elif 90 < angle < 180:
#         return 3

# # 예각, 둔각 테스트 통과
# ==============================================
# def solution(angle):
#     if 0 < angle < 90:
#         return 1
#     elif angle == 90:
#         return 2
#     elif 90 < angle < 180:
#         return 3
#     elif angle == 180:
#         return 4
    
# # 직각 테스트 케이스 추가, 4개 테스트 모두 통과
