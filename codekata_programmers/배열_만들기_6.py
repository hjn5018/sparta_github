# def solution(arr):
#     stk = []
#     i = 0
#     while i < len(arr):
#         if not stk:
#             stk.append(arr[i])
#             i += 1
#         if stk and stk[-1] == arr[i]:
#             stk.pop()
#             i += 1
#         if stk and stk[-1] != arr[i]:
#             stk.append(arr[i])
#             i += 1
#     if stk:
#         return stk
#     else:
#         return [-1]
    # 런타임 에러
    # ---------------------------
# def solution(arr):
#     stk = []
#     i = 0
#     while i < len(arr):
#         if not stk:
#             stk.append(arr[i])
#         if stk and stk[-1] == arr[i]:
#             stk.pop()
#         if stk and stk[-1] != arr[i]:
#             stk.append(arr[i])
#         i += 1
#     if stk:
#         return stk
#     else:
#         return [-1]
#     런타임 에러라기 보다는 그냥 실패
# ----------------------------------
# def solution(arr):
#     stk = []
#     i = 0
#     while i < len(arr):
#         if not stk:
#             stk.append(arr[i])
#             i += 1
#         if stk and stk[-1] == arr[i]:
#             del(stk[-1])
#             i += 1
#         if stk and stk[-1] != arr[i]:
#             stk.append(arr[i])
#             i += 1
#     if stk:
#         return stk
#     else:
#         return [-1]
#     pop이 아니라 del써도 런타임 에러
# ---------------------------------
def solution(arr):
    stk = []
    stk.append(arr[0])
    for i in range(1, len(arr), 2):
        if arr[i] == arr[i-1]:
            stk.pop()
        else:
            stk.append(arr[i])
    return stk
    # 새로운 규칙을 만들기 힘들다..