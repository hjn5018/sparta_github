# n = 12345
# n = 54321


# print(list(str(n)))
# ['1', '2', '3', '4', '5']

# print(sorted(list(str(n)), reverse=True))
# ['5', '4', '3', '2', '1']

# list_ = sorted(list(str(n)), reverse=True)
# list_1 = []
# for i in list_:
#     list_1.append(int(i))

# print(list_1)
# [5, 4, 3, 2, 1]

# n = 12345 인 경우와
# n = 54321 인 경우의 sort reverse가 54321로 동일하다.
# 정렬한다기보다는 뒤집어야한다.
# =================================================
n = 94568

list_ = list(str(n))[::-1]
list_1 = []
for i in list_:
    list_1.append(int(i))

print(list_1)
# [8, 6, 5, 4, 9]