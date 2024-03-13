# A, B = map(int, input().split())
# C = int(input())


# if B + C > 60:
#     A += (B + C) // 60
#     B += C - ((B + C) // 60) * 60
# elif B + C < 60:
#     B += C
# elif B + C == 60 and A == 23:
#     A += 1
#     B == 0
# else: # B + C == 60 and A != 23:
#     A += 1
#     B == 0


# print(A, B)
# 틀렸습니다.
# =============================================
# A, B = map(int, input().split())
# C = int(input())


# if B + C < 60:
#     B += C
# elif B + C > 60:
#     A += ((B + C) // 60)
#     B == ((B + C) % 60)
#     if A >= 24:
#         A -= 24
# else: # B + C == 60:
#     A += 1
#     B == 0
#     if A >= 24:
#         A -= 24


# print(A, B)
# 틀렸습니다.
# ================================================
A, B = map(int, input().split())
C = int(input())


if B + C < 60:
    B += C
elif B + C > 60:
    A += ((B + C) // 60)
    B = ((B + C) % 60)
    if A >= 24:
        A -= 24
else: # B + C == 60:
    A += 1
    B = 0
    if A >= 24:
        A -= 24


print(A, B)
