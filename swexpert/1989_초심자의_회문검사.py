# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.

# [제약 사항]
# 각 단어의 길이는 3 이상 10 이하이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 입력
# 3
# level
# samsung
# eye


# 출력
# #1 1
# #2 0
# #3 1
# ==============인풋 받기 실패===============================================================
# case_num = int(input())
# case = input()
# bash: samsung: command not found
# ==============f스트링 안 했음================================
# case_num = int(input())
# for i, j in enumerate(range(3), 1): # 인풋 다 받아버리기 // enumerate로 index 새겨주기
#     case = input() # 근데 index를 어떻게 꽂아주지..?

#     if case == case[::-1]:
#         print("#{i}, 1")
#     else:
#         print("#{i} 0")
# 3
# level
# #{i} 0
# samsung
# #{i} 0
# eye
# #{i} 0
# ==================palindrome 확인 코드가 잘못됨.???============
# case_num = int(input())
# for i, j in enumerate(range(3), 1): # 인풋 다 받아버리기 // enumerate로 index 새겨주기
#     case = input() # 근데 index를 어떻게 꽂아주지..?

#     if case == case[::-1]:
#         print(f"#{i}, 1")
#     else:
#         print(f"#{i} 0")
# 3
# level
# #1 0
# samsung
# #2 0
# eye
# #3 0
# ==================입력에 띄어쓰기가 섞임=================================
# case_num = int(input())
# for i, j in enumerate(range(3), 1): # 인풋 다 받아버리기 // enumerate로 index 새겨주기
#     case = input() # 근데 index를 어떻게 꽂아주지..?

#     if case == case[::-1]:
#         print(f"#{i}, 1")
#     else:
#         print(f"#{i} {case[::-1]}")
# 3
# level
# #1      level
# samsung
# #2 gnusmas
# eye
# #3  eye
# ===============이제 한번에 출력하기만 하면 됨.=====================================
case_num = int(input())
for i, j in enumerate(range(3), 1): # 인풋 다 받아버리기 // enumerate로 index 새겨주기
    case = input() # 근데 index를 어떻게 꽂아주지..?

    if case == case[::-1]:
        print(f"#{i}, 1")
    else:
        print(f"#{i} 0")
# 3
# level
# #1, 1
# samsung
# #2 0
# eye
# #3, 1
# ======================================================