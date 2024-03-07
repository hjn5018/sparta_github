def solution(arr):
    X = []
    for num in arr:
        for i in range(num):
            X.append(num)
    return X