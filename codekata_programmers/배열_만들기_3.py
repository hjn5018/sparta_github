def solution(arr, intervals):
    answer = []
    for i in intervals:
        a, b = i[0], i[1]
        
        for j in range(a, b + 1):
            answer.append(arr[j])
            
    return answer
# =====================================
# arr = [1, 2, 3, 4, 5]
# intervals = [[1, 3]]
# result = [2, 3, 4]
arr = [1, 2, 3, 4, 5]
intervals = [[1, 3], [0, 4]]
# result = [2, 3, 4, 1, 2, 3, 4, 5]


# for i in intervals:
    # print(i)
    # [1, 3]
    # [0, 4]
    
    # i[1] += 1
    # print(i)
    # [1, 4]
    # [0, 5]
    # for j in range(i):
        # print(j)
        # TypeError: 'list' object cannot be interpreted as an integer
list_ = []
for i in intervals:
    a, b = i[0], i[1]
    # print(a)
    # 1
    # print(b)
    # 3

    # c = range(b) - range(a)
    # TypeError: unsupported operand type(s) for -: 'range' and 'range'
    # print(c)

    # for j in range(a, b):
        # print(j)
        # 1
        # 2
    
    for j in range(a, b + 1):
        list_.append(arr[j])

print(list_)
# [2, 3, 4]
# [2, 3, 4, 1, 2, 3, 4, 5]