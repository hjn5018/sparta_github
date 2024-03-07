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
T = int(input)
list_ = []

for i in range(T):
    case = input()
    for j, letter in enumerate(case, 1): # 근데 str이 iterable인가?
        if letter == case[0]:
            list_.append(j) # 함수에 담아서 return하지 않으면, 어딘가ㅔ 담았다가 뱉어야 하는데..

print(f"#{i} j")

