# ex_list = [x for x in range(3)]
# print(type(ex_list[2]))
# <class 'int'>
# 리스트 컴프리헨션 
# ===============================================
roll_book = [x for x in range(1, 31)]

# print(roll_book)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

for i in range(28):
    student_id = int(input())
    roll_book.remove(student_id)

print(roll_book[0])
print(roll_book[1])
# 2
# 8