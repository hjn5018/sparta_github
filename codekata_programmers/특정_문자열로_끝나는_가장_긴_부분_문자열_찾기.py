myString = "AbCdEFG"
pat = "dE"
# patA = pat + "A"
# myStringA = "AbCdEFGdE"
# result = "AbCdE"

# result = pat in myString
# True

# result = myString.index(pat)
# 3

# result = myString.index(patA)
# ValueError: substring not found

# result = myStringA.index(pat)
# 3

# print(result)
# ==========================================
# def solution(myString, pat):
#     for i in range(len(myString)):
#         if pat in myString[len(myString)-i:]:
#             return myString[:len(myString)-i+len(pat)]
# 오답이 있음.
# ======================================
# def solution(myString, pat):
#     list_ = myString.split(pat)
#     list_A = []
#     for i in range(len(list_)):
#         if pat in list_[i]:
#             list_A.append(i)
            
#     list_ = list_[:max(list_A)+1]
#     return "".join(list_)

# list_ = myString.split(pat)

# print(list_)
# ['AbC', 'FG']
# !!! pat을 포함한 리스트가 아니구나!!!

# list_A = []
# for i in range(len(list_)):
#     if pat in list_[i]:
#         list_A.append(i)

# list_ = list_[:max(list_A)+1]
# # ValueError: max() arg is an empty sequence
# print("".join(list_))
# =================================================
# print(myString[::-1])
# GFEdCbA

# print(myString[1::-1])
# bA

# print(myString[2::-1])
# CbA

# print(myString[2:1:-1])
# C

# print(myString[2:0:-1])
# Cb

# print(myString[-1])
# G

# print(myString[-1::-1])
# GFEdCbA

# print(myString[-2])
# F

# print(myString[-2::-1])
# FEdCbA

# print(myString[-1:-2:-1])
# G

# print(myString[-1:-3:-1])
# GF

# print(myString[-1:-1:-1])
# ???

print(myString[-1:-8:-1])