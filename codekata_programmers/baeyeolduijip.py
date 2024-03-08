# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다.
# num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

# 1 ≤ num_list의 길이 ≤ 1,000
# 0 ≤ num_list의 원소 ≤ 1,000

# def solution(num_list):
#     n = len(num_list)
#     list_i = []
#     for j in range(n-1):
#         for i in range(n-1-j):
#             num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
#     return num_list
#             # list_i.append(i)
#     # return list_i
#     # [0, 1, 2, 3]
        
        

# result = solution([1,2,3,4,5])

# print(result)
# ==========================================================
# li = [1,2,3,4,5]

# n = len(li)

# list_i = []
# # list_j = []
# for i in range(n):
#     list_i.append(i)
#     print(list_i)
#     # for j in range(i):
#     #     list_j.append(j)
#     #     # print(list_j)
# ================풀이==================================================
# 1. 돈다
# - for문을 사용한다. (while은 break걸기 좀 묘함.)

# 1. 적용
# def solution(num_list):
#     n = len(num_list) # range의 범위 설정 준비
#     for i in range(n):
# ==========================================================================
# 2. 순서를 바꾼다.
# - i, j = j, i하면 바뀐다고 함.
# (swap이라는 것도 있는데 내부알고리즘이 또 있는 것 같아서 사용하기 좀..)

# 2. 적용
# def solution(num_list):
#     n = len(num_list) 
#     for i in range(n-1): # n 설정 시 IndexError: list index out of range
#                         # list의 index를 range로 돌 때 맨 끝 인덱스 요소가 없음.
#         num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
#     return num_list

# result = solution([1,2,3,4,5])

# print(result)
# # [2, 3, 4, 5, 1]
# ========================================================================
# 3. 돈다
# 첫번째 원소가 마지막까지 가기는 하는데, 이걸 반복해야함.
# 여기가 문제인데
# 하다보니 됐달까...

# 일단 원하는 건 
# 0 1 2 3 4 돌고
# 0 1 2 3 돌고
# ...
# 0 도는 건데

# 너무 안 돼서
# 일단 하나만이라도 줄여서 돌려보고 싶었음.

# li = [1,2,3,4,5]

# n = len(li)

# list_i = []
# # list_j = []
# for i in range(n):
#     list_i.append(i)
#     print(list_i)
#     # for j in range(i):
#     #     list_j.append(j)
#     #     # print(list_j)

# 위 코드를 보면 list_i의 원소가 하나씩 늘어가는데,
# 비몽사몽하면서 저 늘어가는 걸 반대로 빼버리고 싶다는 생각에  -j해봤음.