# count = 0
# while 1:
#     N = int(input())
#     if N == 0:
#         break

#     num_list = []
#     for i in range(N, 2*N + 1):
#         num_list.append(i)
#         # num_list = [N, N+1, ... 2N]

#     for i in num_list:
#         for j in range(1, i+1):
#             if i % j == 0:
#                 continue
#             else:
#                 count += 1
#     print(count)



# print(list(range(1,2)))
    


# 소수 검증
# a가 소수이려면
# a 이하의 모든 수로 나눴을 때 나머지가 0이 아니다.
a = 1000
for i in range(1, a+1):
    if a % i == 0: # a가 i의 배수인 경우 -> 소수 아님
        break
    
print('소수 아님')

        # 소수 아님.
        