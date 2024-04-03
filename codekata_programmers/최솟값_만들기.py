def solution(A,B):
    # answer = 0
    # while A:
    #     answer += min(A) * max(B)
    #     A = A[:A.index(min(A))] + A[A.index(min(A))+1:]
    #     B = B[:B.index(max(B))] + B[B.index(max(B))+1:]
    # return answer
    # 시간 초과
    # =========================
#     answer = 0
#     A.sort(reverse=True)
#     B.sort()
    
#     while A:
#         answer += A[0] * B[0]
#         A = A[1:]
#         B = B[1:]
#     return answer
# 시간 초과
# ====================================
    answer = 0
    A.sort(reverse=True)
    B.sort()
    
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer