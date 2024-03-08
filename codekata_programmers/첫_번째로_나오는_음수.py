# def solution(num_list):
#     for num in num_list:
#         if num < 0:
#             return num_list.index(num)
#         else:
#             return 
        
# 입력값 〉	[12, 4, 15, 46, 38, -2, 15]
# 기댓값 〉	5
# 실행 결과 〉	실행한 결괏값 -1이 기댓값 5과 다릅니다.
# ==========================================================
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    # if 모든 원소가 0보다 크거나 같다면:
    #     return -1
    return -1