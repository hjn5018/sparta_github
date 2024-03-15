# zZa

word = input()

word = word.lower()
set_word = set(word)

list_word = list(set_word)
print(list_word)

count = [0] * len(list_word)
print(count)

print(word)
for i in range(len(list_word)):
    for j in range(len(word)):
        if (list_word[i] in word[j]) or (list_word[i].upper() in word[j]):
# AttributeError: 'list' object has no attribute 'upper'
            count[i] += 1

print(count)

ccount = 0
for i in range(len(count)):
    if max(count) == count[i]:
        ccount += 1

if ccount >= 2:
    print("?")
else:
    print(list_word[])