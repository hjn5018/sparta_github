# 문제 접근

# T = int(input)
# 테스트 케이스의 개수 T받고

# 문자열 받자.
# case = input()
# 물론 T만큼
# for i in range(T):

# 받은 줄에 대해서 마디를 찾는다.
"""
조건 1. 반복을 찾는다.
입력의 예시부터 해결하자면
첫째 글자가 다음에 나타나기 전까지가 반복된다.
"""

# (if case[0]이 다시 출몰하면??)
# (if case[0] in case???)

# for letter in case:
#     if letter == case[0]:
#         번호 뱉어라.
# ->
# for i, letter in enumerate(case):
#     if letter == case[0]:
#         return i ???(return을 쓸 수 있긴 한가...?)
"""
그럼 이렇게 해서 구한 인덱스를 가지고
마디의 길이가 i임을 알 수 있다.
-끗-
"""
# ==============return???=============================
# T = int(input)

# for i in range(T):
#     case = input()
#     for j, letter in enumerate(case, 1): # 근데 str이 iterable인가?
#         if letter == case[0]:
#             return j # 함수에 담아서 return하지 않으면, 어딘가ㅔ 담았다가 뱉어야 하는데..
# =======================================================
# T = int(input)
# list_ = []

# for i in range(T):
#     case = input()
#     for j, letter in enumerate(case, 1): # 근데 str이 iterable인가?
#         if letter == case[0]:
#             list_.append(j) # 함수에 담아서 return하지 않으면, 어딘가ㅔ 담았다가 뱉어야 하는데..

# print(f"#{i} j")

# 20:58:42 (Runtime error)
# Error Message:
# Memory error occured, (e.g. segmentation error, memory limit Exceed, stack overflow,... etc)
# 20:58:42 null
# 20:58:42 실행을 시작합니다.
# 20:58:42 성공적으로 컴파일 되었습니다.
# 20:58:42 Input data가 없으므로 Sample input으로 테스트됩니다.
# ===================================================
# T = int(input)
# list_ = []

# for i in range(T):
#     case = input()
#     for j, letter in enumerate(case, 1): # 근데 str이 iterable인가?
#         if letter == case[0]:
#             list_.append(j) # 함수에 담아서 return하지 않으면, 어딘가ㅔ 담았다가 뱉어야 하는데..

# print(f"#{i} j")

# 20:59:40 (Runtime error)
# Error Message:
# Memory error occured, (e.g. segmentation error, memory limit Exceed, stack overflow,... etc)
# 20:59:40 null
# 20:59:40 실행을 시작합니다.
# 20:59:40 성공적으로 컴파일 되었습니다.
# 20:59:40 Input data가 없으므로 Sample input으로 테스트됩니다.
# ================================================================

T = int(input())

for i in range(1, T+1):
    test_case = input()
    
    for j in range(30): # 길이가 30이라는 조건이 있다.
        # if test_case[0] == test_case[j] and j != 0:
        #     # j가 마디의 길이
        # 이건 SAMSUNG에 걸림
        
        # 문자열의 길이는 30이고, 마디의 최대 길이는 10이다.
        # 조건에 의해 마디의 각 글자는 최소 3번 등장한다.
        
        # 마디 안에 중복되는 글자가 있으면
        # n번 중복 시 최소 3n번 등장한다.
        
        # 마디 외의 글자는 등장하지 않는다.

        # 따라서 test_case에서 모든 문자는 최소 3번 이상 등장한다.
        # 즉, test_case를 3으로 나누면... 그 안에 무조건 마디가 들어있다.
        
        # 그러므로 그 10자의 안에서 마디를 찾을 수 있다.
        # 그러면 어떻게 찾느냐?
        # 1번 등장하거나 다른 글자에 비해 낮은 빈도로 등장한 글자가 있을 수 있다.
        # 예를 들어서 SAMSUNGSAM에서 SAM은 두번나오고 SUNG은 한 번 나온다.
        # 이를 미루어 보아 SUNG는 마디에 포함됨을 알 수 있다.

        # 그에 반해 SAM은??
        # S처럼 ㅈㅁㄴㅇㄻㄴㅇㄻㄴㅇㄻㄴㅇㄹ

        