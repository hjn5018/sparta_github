# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때,
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
# 다음 줄에는 M개의 수들이 주어지는데,
# 이 수들이 A안에 존재하는지 알아내면 된다.
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

# 예제 입력 1 
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

# 예제 출력 1 
# 1
# 1
# 0
# 0
# 1

# n_list_num = int(input())
# n_list = list(map(int, input().split()))
# m_list_num = int(input())
# m_list = list(map(int, input().split()))

# for num in m_list:
#     if num in n_list:
#         print(1)
#     else:
#         print(0)
# 1
# 1
# 0
# 0
# 1
# ======첫 번째 시도 시간초과==========

# len_n_list = int(input()) # 입력 받기
# n_list = list(map(int, input().split()))
# len_m_list = int(input())
# m_list = list(map(int, input().split()))

# start = 0 # 이진탐색 준비 (start, end, mid)
# end = len_n_list - 1
# mid = (start + end) // 2 

# n_list.sort() # 이진탐색 전 정렬

# for target in m_list: # 이진탐색 시작
#     while start < end: # 여기가 좀 문젠데..
#         if n_list[mid] < target:
#             start = mid + 1
#             mid = (start + end) // 2
#         elif n_list[mid] > target:
#             end = mid - 1
#             mid = (start + end) // 2
#         else: # n_list(mid) == target
#             print(1)
#             break
#     print(0)
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
# 1
# 0
# 0
# 0
# 0
# 0

# ==============================================
# list = [1,2,3,4,5]

# print(max(list))
# 5
# ============두 번째 시도에서는 start end mid를 초기화하지 않아서 제대로 안 된 듯.=====================================
# len_n_list = int(input()) # 입력 받기
# n_list = list(map(int, input().split()))
# len_m_list = int(input())
# m_list = list(map(int, input().split()))

# n_list.sort() # 이진탐색 전 정렬

# for target in m_list: # 이진탐색 시작
#     start = 0 # 이진탐색 준비 (start, end, mid)
#     end = len_n_list - 1
#     mid = (start + end) // 2 

#     while start < end: # 여기가 좀 문젠데..
#         if n_list[mid] < target:
#             start = mid + 1
#             mid = (start + end) // 2
#         elif n_list[mid] > target:
#             end = mid - 1
#             mid = (start + end) // 2
#         else: # n_list(mid) == target
#             print(1)
#             break
#     print(0) # 여기도 좀?? 위치가..?
# 1
# 0
# 1
# 0
# 0
# 0
# 0
# =====================print가 아니고 return으로 하면 좀 다르려나?================================================================
# len_n_list = int(input()) # 입력 받기
# n_list = list(map(int, input().split()))
# len_m_list = int(input())
# m_list = list(map(int, input().split()))

# def binary_search(len_n_list, n_list, m_list):
#     n_list.sort() # 이진탐색 전 정렬

#     for target in m_list: # 이진탐색 시작
#         start = 0 # 이진탐색 준비 (start, end, mid)
#         end = len_n_list - 1
#         mid = (start + end) // 2 

#         while start < end: # 여기가 좀 문젠데..
#             if n_list[mid] < target:
#                 start = mid + 1
#                 mid = (start + end) // 2
#             elif n_list[mid] > target:
#                 end = mid - 1
#                 mid = (start + end) // 2
#             else: # n_list(mid) == target
#                 return 1
#         return 0 # 여기도 좀?? 위치가..?

# binary_search(len_n_list, n_list, m_list)
# ???????? 리턴이라 출력 한 되나...

# print(binary_search(len_n_list, n_list, m_list))
# 1
# 1 나오고 끝이라...
# ================한결 튜터님 세션 자료 보고 다시 해보자..===========================================
# 아.. start < end 에서 = 를 빼먹어서 그런가..?????

# len_n_list = int(input()) # 입력 받기
# n_list = list(map(int, input().split()))
# len_m_list = int(input())
# m_list = list(map(int, input().split()))

# n_list.sort() # 이진탐색 전 정렬

# for target in m_list: # 이진탐색 시작
#     start = 0 # 이진탐색 준비 (start, end, mid)
#     end = len_n_list - 1
#     mid = (start + end) // 2 

#     while start <= end: # 여기가 좀 문젠데..
#         if n_list[mid] < target:
#             start = mid + 1
#             mid = (start + end) // 2
#         elif n_list[mid] > target:
#             end = mid - 1
#             mid = (start + end) // 2
#         else: # n_list(mid) == target
#             print(1)
#             break
#     print(0) # 여기도 좀?? 위치가..?
# 1
# 0
# 1
# 0
# 0
# 0
# 1
# 0
# 허허........
# ???????????????????????????? 근데 튜터님 binary랑 큰 차이가 없는데...
# 이 문제의 상황 때문에 그런 것 같은데..
# ======================break도 튜터님 코드랑 다른데 ㄱㄱ===================================
# len_n_list = int(input()) # 입력 받기
# n_list = list(map(int, input().split()))
# len_m_list = int(input())
# m_list = list(map(int, input().split()))

# n_list.sort() # 이진탐색 전 정렬

# for target in m_list: # 이진탐색 시작
#     start = 0 # 이진탐색 준비 (start, end, mid)
#     end = len_n_list - 1
#     mid = (start + end) // 2 

#     while start <= end: # 여기가 좀 문젠데..
#         if n_list[mid] < target:
#             start = mid + 1
#             mid = (start + end) // 2
#         elif n_list[mid] > target:
#             end = mid - 1
#             mid = (start + end) // 2
#         else: # n_list(mid) == target
#             print(1)
#     print(0) # 여기도 좀?? 위치가..?

# 아........................
# 내 거는 break가 필요한데.............
# ========================다시 짜보자============================================

# N = int(input())
# A_list = list(map(int, input().split())) # 탐색될 요소들의 리스트
# M = int(input())
# B_list = list(map(int, input().split())) # 타겟이 모인 리스트

# start = 0
# end = N - 1 # 2-A. 이진탐색을 할거고, index로 start, end를 설정할 때 end는 len - 1이다.

# A_list.sort() # 2. 반복문 들어가기 전에 이진탐색을 위한 정렬부터

# for target in B_list: # 1. B_list를 돌면서 확인할건데
# #     print(target)
# # 1
# # 3
# # 7
# # 9
# # 5
#     while start <= end: # 2-1. 이진탐색 들어가는데, end start 엇갈리면 target 없는거 
#         mid = (start + end) // 2 # 2-B 이진탐색의 기준점(mid)은 시행마다 달라진다. -> while문 안에 넣기.
#         if target > A_list[mid]: # up인 경우
#             start = mid + 1
#         elif target < A_list[mid]:
#             end = mid + 1
#         else: # target == A_list[mid] 리스트 안에 target이 존재하는 경우
#             print(1)
#     print(0) # start > end인 경우(로직을 벗어난 경우//탐색을 다 한 경우)

# ????????? 엔터 쳐도 안 넘어가는데???????????????//
    

# 85 - 107번줄과 비교하자
# =====================왜 안 넘어갈까.. 1 2 3 4 입력하면 잘 되는데..====================================
# N = int(input())
# A_list = list(map(int, input().split())) # 탐색될 요소들의 리스트
# M = int(input())
# B_list = list(map(int, input().split())) # 타겟이 모인 리스트

# start = 0
# end = N - 1 # 2-A. 이진탐색을 할거고, index로 start, end를 설정할 때 end는 len - 1이다.

# A_list.sort() # 2. 반복문 들어가기 전에 이진탐색을 위한 정렬부터

# for target in B_list: # 1. B_list를 돌면서 확인할건데
#     # print(target)
# # 1
# # 3
# # 7
# # 9
# # 5
#     while start <= end: # 2-1. 이진탐색 들어가는데, end start 엇갈리면 target 없는거 
#         mid = (start + end) // 2 # 2-B 이진탐색의 기준점(mid)은 시행마다 달라진다. -> while문 안에 넣기.
#         if target > A_list[mid]: # up인 경우
#             start = mid + 1
#         elif target < A_list[mid]:
#             end = mid - 1
#         else: # target == A_list[mid] 리스트 안에 target이 존재하는 경우
#             print(1)
#     print(0) # start > end인 경우(로직을 벗어난 경우//탐색을 다 한 경우)

# print(N)
# 5
# print(n)
# NameError: name 'n' is not defined
# print(A_list)
# [4, 1, 5, 2, 3]
# print(M)
# 5
# print(B_list)
# [1, 3, 7, 9, 5]
# print(A_list) # .sort() 한 경우
# [1, 2, 3, 4, 5]
    
# 여기까진 잘 되는데.. 왜 돌질 않니???????????
# 일단 for문부터가 문제인 듯 한데...
# for문과 while 사이의 주석이 문제는 아닌 걸 확인했고..

# 그럼 while이 문제인데..
# 아... end + 1을 해버렸네..........

# 근데 또 무한 1111111111111111111111111111111
# ===================다시 작성해도 같달까...=============================================
N = int(input())
A_list = list(map(int, input().split())) # 탐색될 요소들의 리스트
M = int(input())
B_list = list(map(int, input().split())) # 타겟이 모인 리스트

start = 0
end = N - 1 # 2-A. 이진탐색을 할거고, index로 start, end를 설정할 때 end는 len - 1이다.

A_list.sort() # 2. 반복문 들어가기 전에 이진탐색을 위한 정렬부터

for target in B_list: # 1. B_list를 돌면서 확인할건데
    # print(target)
# 1
# 3
# 7
# 9
# 5
    while start <= end: # 2-1. 이진탐색 들어가는데, end start 엇갈리면 target 없는거 
        mid = (start + end) // 2 # 2-B 이진탐색의 기준점(mid)은 시행마다 달라진다. -> while문 안에 넣기.
        if target > A_list[mid]: # up인 경우
            start = mid + 1
        elif target < A_list[mid]:
            end = mid - 1
        else: # target == A_list[mid] 리스트 안에 target이 존재하는 경우
            print(1)
            break
    print(0) # start > end인 경우(로직을 벗어난 경우//탐색을 다 한 경우)
# 1
# 0
# 0
# 0
# 0
# 0
# break 넣었더니 다시 원점.............................
