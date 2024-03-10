# def solution(arr, delete_list):
#     for num in delete_list:
#         if num in arr:
#             arr.delete(num)
#     return arr
# AttributeError: 'list' object has no attribute 'delete'

# def solution(arr, delete_list):
#     for num in delete_list:
#         if num in arr:
#             arr.pop(num)
#     return arr
# IndexError: pop index out of range

# def solution(arr, delete_list):
#     new_arr = []
#     for i in range(len(delete_list)):
#         if delete_list[i] not in arr:
#             new_arr.append(arr[i])
#     return new_arr
# IndexError: list index out of range

# delete_list랑 arr 길이가 다르구낭.. ㅎㅎ

def solution(arr, delete_list):
    new_arr = []
    for num in arr:
        if num not in delete_list:
            new_arr.append(num)
    return new_arr