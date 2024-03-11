# for _ in range(10):
#     test_num = int(input())
#     list_ = []
    
#     list_.append(test_num//42)

# set_ = set(list_)

# print(len(set_))
# 틀렸습니다.
# =============================
# list_ = []
# for _ in range(10):
#     test_num = int(input())
    
#     list_.append(test_num//42)

# set_ = set(list_)

# print(len(set_))
# 틀렸습니다.
# =================================
list_ = []
for _ in range(10):
    test_num = int(input())
    
    list_.append(test_num % 42)

set_ = set(list_)

print(len(set_))