# A_code
def solution(arr, n):
    if len(arr) % 2 == 1:
        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] = arr[i] + n
    else:
        for i in range(len(arr)):
            if i % 2 == 1:
                arr[i] = arr[i] + n
    return arr
# ============================================
# B_code
def solution(arr, n):
    len_arr = len(arr)
    if len_arr % 2 == 1:
        for i in range(len_arr):
            if i % 2 == 0:
                arr[i] == arr[i] + n
    else:
        for i in range(len_arr):
            if i % 2 == 1:
                arr[i] == arr[i] + n
    return arr

arr = [49, 12, 100, 276, 33]
n = 27
right_answer = [76, 12, 127, 276, 60]

result = solution(arr, n)

print(result)
# A_code
# [76, 12, 127, 276, 60]

# B_code
# [49, 12, 100, 276, 33]