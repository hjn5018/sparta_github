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
# case_num = int(input())
# for i, j in enumerate(range(3), 1): # 인풋 다 받아버리기 // enumerate로 index 새겨주기
#     case = input() # 근데 index를 어떻게 꽂아주지..?

#     if case == case[::-1]:
#         print(f"#{i}, 1")
#     else:
#         print(f"#{i} 0")
# 3
# level
# #1, 1
# samsung
# #2 0
# eye
# #3, 1
# ============str_에 담는 건 아닌듯.. 계속 초기화 될 뿐임..==========================================
# case_num = int(input())
# str_ = ""

# for i, j in enumerate(range(3), 1): # 인풋 다 받아버리기 // enumerate로 index 새겨주기
#     case = input() # 근데 index를 어떻게 꽂아주지..?

#     if case == case[::-1]:
#         str_ + f"#{i}, 1"
#         # print(f"#{i}, 1")
#     else:
#         str_ + f"#{i}, 0"
#         # print(f"#{i} 0")
# =========================7/10 오답=================================
# case_num = int(input())
# list_ = []

# for i, j in enumerate(range(3), 1): # 인풋 다 받아버리기 // enumerate로 index 새겨주기
#     case = input() # 근데 index를 어떻게 꽂아주지..?

#     if case == case[::-1]:
#         list_.append(f"#{i} 1")
#         # list_.append(f"#{i}, 1")
#         # print(f"#{i}, 1")
#     else:
#         list_.append(f"#{i} 0")
#         # list_.append(f"#{i}, 0")
#         # print(f"#{i} 0")

# for k in list_:
#     print(k)

#1, 1
#2, 0
#3, 1
# 콤마 떼자!!!
#1 1
#2 0
#3 1

# 오답
# 채점용 input 파일로 채점한 결과 fail 입니다.
# (오답 : 10개의 테스트케이스 중 3개가 맞았습니다.)
# ========================================================
