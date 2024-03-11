# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# 기억나는 대로 작성함
# 틀림
# =================================================
# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# 탈출 수정
# 틀림
# ====================================================
# n = int(input())

# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# 인풋 설정
# 틀림
# ====================================================
# n = int(input())

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# 0번째가 0이라고 해서 탈출 재수정
# 틀림
# ======================================================
# n = int(input())

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-2) + fibonacci(n-1)
    

# # n = 2
# # 1

# # n = 3
# # 2
# # result = fibonacci(n)

# # print(result)

# # 호출을 안 했네
# fibonacci(n)
# # 틀림
# =================================================================
# n = int(input())

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-2) + fibonacci(n-1)

# result = fibonacci(n)

# print(result)
# 시간 초과
# n = 10 일때 55 제대로 나옴
# ===============================================
# n = int(input())

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         print(fibonacci(n-2) + fibonacci(n-1))

# 함수에 바로 프린트 박아버리기
# 틀림

# n = 10일 때 출력 아무 것도 없음
# ==============================================
n = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(n))

# result 생성 안 하고 바로 print 해보기
# 시간 초과