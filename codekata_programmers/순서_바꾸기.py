def solution(num_list, n):
    # num_list[n:].append(num_list[:n]).pop
    # new_list = []
    # new_list.append(num_list[n:])
    # new_list.append(num_list[:n])
    # return new_list
# 실행한 결괏값 [[1,6],[2]]이 기댓값 [1,6,2]과 다릅니다.
# ========================================================
    after = num_list[n:]
    before = num_list[:n]
    new_list = []
    
    for i in after:
        new_list.append(i)
    for i in before:
        new_list.append(i)
    return new_list