my_string = "Bcad"

# print(list(my_string.lower()).sort())
# None

# print(list(my_string.lower()))
# ['b', 'c', 'a', 'd']

# print(sorted(list(my_string.lower())))
# ['a', 'b', 'c', 'd']

# print(str(sorted(list(my_string.lower()))))
# ['a', 'b', 'c', 'd']

my_string = sorted(list(my_string.lower()))

result = ''
for i in my_string:
    result += i

print(result)




# str(list(my_string.lower()).sort())
