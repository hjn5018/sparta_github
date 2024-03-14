import sys

sys.stdin = open('input.txt')

T = int(input())
# opne('input.txt') 사용 시
# ValueError: invalid literal for int() with base 10: ''

# T = int(sys.stdin.readline().rstrip('\n').rstrip(''))
# ValueError: invalid literal for int() with base 10: ''
#     T = int(sys.stdin.readline())
# ValueError: invalid literal for int() with base 10: '\n'
#     T = int(sys.stdin.readline().rstrip('\n'))
# ValueError: invalid literal for int() with base 10: ''

def allocate(x, y): # x > y인 경우
    x -= y
    y += y
    return x, y


for i in range(1, T+1):
    A, B, K = map(int, input().split())
    # A, B, K = map(int, sys.stdin.readline().split())

    for _ in range(K):
        if A > B:
            A, B = allocate(A, B)
        elif A < B:
            B, A = allocate(B, A)
        else: # A == B:
            A = 0
            B = A + B

        result = min(A, B)
    print(f"#{i} {result}")
# 4
# 4 9 1
# #1 4
# 4 9 2
# #2 4
# 4 9 3
# #3 4
# 500 2000 2000000000
# 너무 오래 걸림