# dial_dict = {
#     'ABC':2, 'DEF':3, 'GHI':4, 'JKL':5,
#     'MNO':6, 'PQRS':7, 'TUV':8, 'WXYZ':9,
#     }
# print('A' in dial_dict)
# # False
# ==============================================
# dial_dict = {
#     'A','B','C':2
#     }
# # SyntaxError: invalid syntax
# print('A' in dial_dict)
# =================================================
# word = input()

# sum = 0
# for i in range(len(word)):
#     if word[i] in ???:
#         word[i] = ???? # 숫자
#     sum += word[i]+1

# print(sum)

# ================================================
alpabet_list = []
for i in range(97, 123):
    alpabet_list.append(chr(i))

# print(alpabet_list)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dial_index = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
# dial_dict = {
    
# }

word = input()

dial_dict = {}
for i in range(len(range(97, 123))):
    k, v = chr(i+97), dial_index[i]
    dial_dict[f'{chr(i+97)}'] = dial_index[i]
# print(dial_dict)
# {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9}

into_num = []
for i in range(len(word)):
    if word[i] in dial_dict:
        # into_num.append(dial_dict[word[i]]+1)
        # []
        into_num.append(1)
        # []
print(into_num)
