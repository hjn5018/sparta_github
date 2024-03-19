# def solution(num, k):
#     result = 0
#     for i in str(num):
#         # TypeError: 'int' object is not iterable
#         if int(i) == k:
#             result = str(num).index(i)
#             return result
#         else:
#             return -1
# ========================================
# num = 29183
# k = 1


# result = 0
# for i in str(num):
#     # TypeError: 'int' object is not iterable
#     if int(i) == k:
#         result = str(num).index(i)
#         print(result)
#     continue
# print(-1)
# ===============================================
def solution(num, k):
    result = 0
    for i in str(num):
        # TypeError: 'int' object is not iterable
        if int(i) == k:
            result = (str(num).index(i)) + 1
            return result
    return -1