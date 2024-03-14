def solution(array):
    # answer = []
    # answer.append(max(array))
    # answer.append(array.index(max(array)))
    
    # answer = [0, 0]
    # max = 0
    # for i, j in enumerate(array):
    #     if j > max:
    #         max = j
    #         answer[0] = max
    #         answer[1] = i
    
    max = 0
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            # answer[0] = max
            # answer[1] = i
            answer = [array[i], i]
    return answer