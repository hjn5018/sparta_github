# A, B = int(input())

# print(A + B)
# 런타임 에러 (ValueError)
# =====================
A, B = map(int, input().split())

print(A + B)
