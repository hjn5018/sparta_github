# while True:
#     A, B = map(int, input().split())

#     print(A+B)
# sys open 쓸 때
# 런타임 에러 (EOFError)

# 복붙할 때
# ValueError: not enough values to unpack (expected 2, got 0)
# ====================================================
# while True:
#     A, B = map(int, input().split())
#     # ValueError: not enough values to unpack (expected 2, got 0)
#     if A == "" and B == "":
#         break
    
#     print(A+B)
# =================================================
# while True:
#     if A != "" and B != "":
#         # NameError: name 'A' is not defined
#         A, B = map(int, input().split())
    
#     print(A+B)
# ===================================================
# while True:
#     try:
#         A, B = map(int, input().split())
#     except ValueError:
#         break
#     # 런타임 에러 (EOFError)
#     print(A+B)
# 1 1
# 2
# 2 3
# 5
# 3 4
# 7
# 9 8
# 17
# 5 2
# 7
# 빈 칸
# 빈 칸

# ============================================
# import sys

# sys.stdin = open('input.txt')

# while True:
#     try:
#         A, B = map(int, input().split())
#     except ValueError:
#         break
#     # 런타임 에러 (EOFError)
#     print(A+B)

# EOFError: EOF when reading a line
# ==================================================
# import sys

# sys.stdin = open('input.txt')

# while A, B = map(int, input().split()):
# #   File "10951_A+B-4.py", line 48
# #     while A, B = map(int, input().split()):
# #           ^
# # SyntaxError: invalid syntax
#     print(A+B)
# ================================================
# import sys

# sys.stdin = open('input.txt')

# while input():
#     A, B = map(int, input().split())
#     print(A+B)
# 5
# 17
# Traceback (most recent call last):
#   File "10951_A+B-4.py", line 57, in <module>
#     A, B = map(int, input().split())
# EOFError: EOF when reading a line
# ==================================================
# import sys

# sys.stdin = open('input.txt')

# while list(map(int, input().split())):
#     A, B = map(int, input().split())
#     print(A+B)
# 5
# 17
# Traceback (most recent call last):
#   File "10951_A+B-4.py", line 71, in <module>
#     A, B = map(int, input().split())
# EOFError: EOF when reading a line
# ===================================================
# import sys

# sys.stdin = open('input.txt')

# while list(map(int, input().split())):
#     A, B = list[0], list[1]
#     # TypeError: 'type' object is not subscriptable
#     print(A+B)
# =========================================================
# import sys

# sys.stdin = open('input.txt')

# while list(map(int, input().split())):
#     A, B = list[0], list[1]
#     # TypeError: 'type' object is not subscriptable
#     print(A+B)
# =========================================================
# import sys

# sys.stdin = open('input.txt')

# while input() is not None:
#     A, B = list(map(int, input().split())) 
#     print(A+B)
# 5
# 17
# Traceback (most recent call last):
#   File "10951_A+B-4.py", line 106, in <module>
#     A, B = list(map(int, input().split()))
# EOFError: EOF when reading a line
# ===================================================
# import sys

# sys.stdin = open('input.txt')

# while input() is not None:
#     A, B = list(map(int, input().split())) 
#     print(A+B)
# ===================================================
# while True:
#     try:
#         A, B = map(int, input().split())
#     except ValueError:
#         pass
#     # 런타임 에러 (EOFError)
#     print(A+B)
# 1 1
# 2
# 2 3
# 5
# 3 4
# 7
# 9 8
# 17
# 5 2
# 7

# 7

# 7
# ===============================================
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break
# 1 1
# 2
# 2 3
# 5
# 3 4
# 7
# 9 8
# 17
# 5 2
# 7

# Traceback (most recent call last):
#   File "10951_A+B-4.py", line 164, in <module>
#     a, b = map(int, input().split())
# ValueError: not enough values to unpack (expected 2, got 0)