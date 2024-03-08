# def solution(start, end_num):
#     for num in range(end_num, start+1, -1):
#         return num
# range의 step에서는 index처럼 역순으로 갈 수가 없다????
# ==========================================
def solution(start, end_num):
    list_ = []
    for num in range(end_num, start+1):
        list_.append(num)
    return list_[::-1]