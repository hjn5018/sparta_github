# N, M = map(int, input().split())

# bowl_list = []
# for _ in range(N):
#     bowl_list.append(0)

# # print(bowl_list)
# # [0, 0, 0, 0, 0]
    
# for _ in range(M):
#     i, j, k = map(int, input().split())

#     for bowl in bowl_list[i:j+1]:
#         bowl = k

# print(bowl_list)
# [0, 0, 0, 0, 0]
# =====================================
# N, M = map(int, input().split())

# bowl_list = []
# for _ in range(N):
#     bowl_list.append(0)

# for _ in range(M):
#     i, j, k = map(int, input().split())

#     for bowl in bowl_list[i:j+1]:
#         bowl = k
#         print(bowl_list)
# 5 4
# 1 2 3
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# 3 4 4
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# 1 4 1
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# 2 2 2
# [0, 0, 0, 0, 0]
# ==================================
# tuple_ = (1, 2)

# print(tuple_)
# (1,2 )

# print(tuple_[1])
# 2

# tuple_[1] = 3

# print(tuple_[1])
# TypeError: 'tuple' object does not support item assignment
# =========================================
# N, M = map(int, input().split())

# bowl_list = []
# for _ in range(N):
#     bowl_list.append(0)

# for _ in range(M):
#     i, j, k = map(int, input().split())

#     # for bowl in bowl_list[i:j+1]:
#     #     bowl = k
#     bowl_list[i:j+1] = k
#     print(bowl_list)
# bowl_list[i:j+1] = k
# TypeError: can only assign an iterable
    
# =====================================
# N, M = map(int, input().split())

# bowl_list = []
# for _ in range(N):
#     bowl_list.append(0)

# for _ in range(M):
#     i, j, k = map(int, input().split())
#     k_ball_list = []
    
#     for _ in range(j-i+1):
#         k_ball_list.append(k)
    
#     bowl_list[i:j+1] = k_ball_list

#     print(bowl_list)
# 5 4
# 1 2 3
# [0, 3, 3, 0, 0]
# 3 4 4
# [0, 3, 3, 4, 4]
# 1 4 1
# [0, 1, 1, 1, 1]
# 2 2 2
# [0, 1, 2, 1, 1]
    
# 바구니 번호 매기기가 1번부터 5번임. 0번 부터 시작했으니까 한 칸 밀렸음
# ================================================
# N, M = map(int, input().split())

# bowl_list = []
# for _ in range(N):
#     bowl_list.append(0)

# for _ in range(M):
#     i, j, k = map(int, input().split())
#     k_ball_list = []
    
#     for _ in range(j-i+1):
#         k_ball_list.append(k)
    
#     bowl_list[i-1:j] = k_ball_list
#     # 번호 매기기 수정

#     # print(bowl_list)
# print(" ".join(bowl_list))
# TypeError: sequence item 0: expected str instance, int found
# ==================================================
# N, M = map(int, input().split())

# bowl_list = []
# for _ in range(N):
#     bowl_list.append(0)

# for _ in range(M):
#     i, j, k = map(int, input().split())
#     k_ball_list = []
    
#     for _ in range(j-i+1):
#         k_ball_list.append(k)
    
#     bowl_list[i-1:j] = k_ball_list
#     # 번호 매기기 수정

#     # print(bowl_list)

# for l in bowl_list:
#     l = str(l)
# # join 사용 준비
    
# print(" ".join(bowl_list))
# TypeError: sequence item 0: expected str instance, int found
# for l in bowl_list:
#     l = str(l) 가 소용 없었음
# ==============================================
# num_list = [1, 2, 3, 4]

# for l in num_list:
#     l = l + 2

# print(num_list)
# [1, 2, 3, 4]
# for l in range(len(num_list)):
#     num_list[l] += 2

# print(num_list)
# [3, 4, 5, 6]

# for l in range(len(num_list)):
#     num_list[l] = str(num_list[l])

# print(num_list)
# ['1', '2', '3', '4']
# ============================================
# N, M = map(int, input().split())

# bowl_list = []
# for _ in range(N):
#     bowl_list.append(0)

# for _ in range(M):
#     i, j, k = map(int, input().split())
#     k_ball_list = []
    
#     for _ in range(j-i+1):
#         k_ball_list.append(k)
    
#     bowl_list[i-1:j] = k_ball_list
#     # 번호 매기기 수정

#     # print(bowl_list)

# for l in range(len(bowl_list)):
#     bowl_list[l] = str(bowl_list[l])
# # join 사용 준비
    
# print(" ".join(bowl_list))
# # 1 2 1 1 0
# =================================================
N, M = map(int, input().split())

bowl_list = []
for _ in range(N):
    bowl_list.append(0)

for _ in range(M):
    i, j, k = map(int, input().split())
    k_ball_list = []
    
    for _ in range(j-i+1):
        k_ball_list.append(k)
    
    bowl_list[i-1:j] = k_ball_list
    # 번호 매기기 수정

    # print(bowl_list)

# for l in range(len(bowl_list)):
#     bowl_list[l] = str(bowl_list[l])
# join 사용 준비
    

bowl_list = [str(x) for x in bowl_list]
# list comprehension 사용해보기
# 성공

print(" ".join(bowl_list))
# 1 2 1 1 0
