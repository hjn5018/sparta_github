# S = input()

# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# for i in range(len(alphabet)):
#     if alphabet[i] in S:
#         alphabet[i] = str(i) + " "
#         # TypeError: 'str' object does not support item assignment
#     else:
#         alphabet[i] = str(-1) + " "

# print(alphabet)
# ===========================================
# S = input()

# alphabet_list = [x for x in chr[97:127]]
# # TypeError: 'builtin_function_or_method' object is not subscriptable

# print(alphabet_list)
# ===============================================
# print(chr[97:127])
# TypeError: 'builtin_function_or_method' object is not subscriptable
# ============================================
# S = input()

# alphabet_list = [chr(x) for x in range(97, 123)]
# # print(alphabet_list)
# # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for i in range(len(alphabet_list)):
#     if alphabet_list[i] in S:
#         alphabet_list[i] = str(i)
#     else:
#         alphabet_list[i] = str(-1)
# # print(alphabet_list)
# # ['0', '1', '-1', '-1', '4', '-1', '-1', '-1', '-1', '9', '10', '-1', '-1', '13', '14', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1']

# result = " ".join(alphabet_list)

# print(result)
# # 0 1 -1 -1 4 -1 -1 -1 -1 9 10 -1 -1 13 14 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1        
# ==============================================================================
S = input()

alphabet_list = [chr(x) for x in range(97, 123)]
# print(alphabet_list)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(alphabet_list)):
    if alphabet_list[i] in S:
        alphabet_list[i] = str(S.index(alphabet_list[i]))
    else:
        alphabet_list[i] = str(-1)
# print(alphabet_list)

result = " ".join(alphabet_list)

print(result)
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1