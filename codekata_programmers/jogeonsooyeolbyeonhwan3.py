# 정수 배열 arr와 자연수 k가 주어집니다.

# 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, k가 짝수라면 arr의 모든 원소에 k를 더합니다.

# 이러한 변환을 마친 후의 arr를 return 하는 solution 함수를 완성해 주세요.

# 1 ≤ arr의 길이 ≤ 1,000,000
# 1 ≤ arr의 원소의 값 ≤ 100
# 1 ≤ k ≤ 100

# arr = [1, 2, 3, 100, 99, 98]
# k = 3

# def solution(arr, k):
#     if k % 2 == 1:
#         arr * 2
#     else:
#         arr + k
#     return arr
# TypeError: can only concatenate list (not "int") to list


# print(solution(arr, k))
# [1, 2, 3, 100, 99, 98]
# ?????????????????
# ===============================
#create an array
# a = [3, 14, 8, 2, 7, 5]
# print(len(a))
# 6
#access every other element
# for i in range(0, len(a)):
#     print(a[i])

# print(a[6])
# IndexError: list index out of range
# ========================================

# def solution(arr, k):
#     if k % 2 == 1:
#         arr * 2
#     else:
#         arr + k
#     return arr

# arr = [1, 2, 3, 100, 99, 98]
# k = 3

# if k % 2 == 1:
#     arr * 2
# else:
#     arr + k
# print(arr)
# [1, 2, 3, 100, 99, 98]
# 바로 곱해버리기 x
# =============================================
# new_arr = []
# if k % 2 == 1:
#     for num in arr:
#         new_arr.append(num * 2)
# else:
#     for num in arr:
#         new_arr.append(num + k)

# print(new_arr)
# ==============================================
# def solution(arr, k):
#     new_arr = []
    
#     if k % 2 == 1:
#         for num in arr:
#             new_arr.append(num * 3)
#     else:
#         for num in arr:
#             new_arr.append(num + k)
    
#     return new_arr

# arr = [1, 2, 3, 100, 99, 98]
# k = 3
# # [3, 6, 9, 300, 297, 294]

# arr = [1, 2, 3, 100, 99, 98]
# k = 2
# # [3, 4, 5, 102, 101, 100]

# result = solution(arr, k)

# print(result)

# # 테스트 절반 실패(인자자리에서 연산해도 되긴 함.)
# ======================================================
# def solution(arr, k):
#     new_arr = []
    
#     if k % 2 == 1:
#         for num in arr:
#             new_arr.append(num * 3)
#     elif k % 2 == 0:
#         for num in arr:
#             new_arr.append(num + k)
#     arr = new_arr
#     return arr

# 쪼잔하게 arr를 리턴하라는 것 때문에 오답내진 않았음.
# else의 문제도 아닌 것 같음.
# ======================================================
# 각 분기마다 return을 넣어야하나..

def solution(arr, k):
    new_arr = []
    
    if k % 2 == 1:
        for num in arr:
            new_arr.append(num * 3)
        return new_arr
    else:
        for num in arr:
            new_arr.append(num + k)
        return new_arr

# 그래도 아니야...
# ================================================
# def solution(arr, k):
#     if k % 2 == 1:
#         for i in arr:
#             i * k
#     else:
#         for j in arr:
#             j + k
#     return arr

# 하.. i *= k라던지 i = i * k라던지
# 복잡하게 하기 싫은데...
# ===================================================
# def solution(arr, k):
#     if k % 2 == 1:
#         for i in arr:
#             i = i * k
#     else:
#         for j in arr:
#             j = j + k
#     return arr

# 근데 그래도 안 되는 건 뭔데???
# =======================================
def solution(arr, k):
    new_arr = []
    
    if k % 2 == 1:
        for i in arr:
            i = i * k
            new_arr.append(i)
    else:
        for j in arr:
            j = j + k
            new_arr.append(j)
            
    return new_arr

# 승질 뻗치게 하네??

# ===================================

l = [2,2,2,2]

# print(len(l))
# 4

o = [1,3,6,9,18]

# for i in [1,3,6,9,18]:
#     i*3
# print(o)
# [1, 3, 6, 9, 18]

# for i in o:
#     i*3
# print(o)
# [1, 3, 6, 9, 18]

# for i in o:
#     i = i*3
# print(o)
# [1, 3, 6, 9, 18]

# for i in o:
#     print(i)
# 1
# 3
# 6
# 9
# 18

# for i in o:
#     print(o[i])
# IndexError: list index out of range
    
# p = [3]
# for i in p:
#     print(p[i])
# IndexError: list index out of range
    

# ==============================================
def solution(arr, k):
    new_arr = []
    
    if k % 2 == 1:
        for i in arr:
            new_arr.append(i*k)
    else:
        for j in arr:
            new_arr.append(j+k)
            
    return new_arr
# ========================================
def solution(arr, k):
    new_arr = []
    
    if k % 2 == 1:
        for i in arr:
            new_arr.append(i * k)
    else:
        for i in arr:
            new_arr.append(i + k)
            
    return new_arr
# ==========================================
def solution(arr, k):
    new_arr = []
    
    if k % 2 == 1:
        for i in arr:
            new_arr.append(i*k)
    else:
        for j in arr:
            new_arr.append(j+k)
            
    return new_arr
# ================================================
# 띄어쓰기의 문제도 아니고,
# 변수의 문제도 아니면...

# dk..................................
# k 대신에 3 넣어서.........................
# 예시가 내 눈 앞을 가려버리네
# ㅂㄹ뱢로뱢로ㅑㅂㅈ로ㅔㅑㅂ조레ㅑㅗ