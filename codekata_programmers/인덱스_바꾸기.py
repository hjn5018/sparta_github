# # def solution(my_string, num1, num2):
# #     my_string += 'a'
# #     my_string[-1] = my_string[num1]
# #     return my_string[-1]


# my_string = "hello"
# num1 = 1
# num2 = 2

# # my_string.replace(my_string[num2], my_string[num1])
# # my_string_num1 = my_string[num1]
# # my_string_num2 = my_string[num2]
# # print(my_string_num1)
# # print(my_string_num2)

# my_string += 'a'
# # helloa

# my_string = my_string.replace(my_string[-1], my_string[num1])
# # helloe

# # my_string = my_string.replace(my_string[num1], my_string[num2])
# # hlllol

# my_string = my_string.replace(my_string[num1], my_string[num2], 1)
# # hllloe

# my_string = my_string.replace(my_string[num2], my_string[-1], 1)
# # helloe


# # my_string = my_string[:len(my_string)-1]



# print(my_string)
# # print(my_string[-1])
# # print(my_string[num1])
# ========================================================
# my_string = "hello"
# num1 = 1
# num2 = 2
# result = "hlelo"

my_string = "I love you"
num1 = 3
num2 = 6
# result = "I l veoyou"

# my_string = list(my_string)
# print(my_string)
# ['h', 'e', 'l', 'l', 'o']

# my_string = my_string.split()
# print(my_string)
# ['hello']


my_string = list(my_string)
my_string += my_string[num1]
# print(my_string)
# ['h', 'e', 'l', 'l', 'o', 'e']

my_string[num1] = my_string[num2]
# print(my_string)
# ['h', 'l', 'l', 'l', 'o', 'e']

my_string[num2] = my_string[len(my_string)-1]
# print(my_string)
# ['h', 'l', 'e', 'l', 'o', 'e']

my_string = my_string[:len(my_string)-1]
# print(my_string)
# ['h', 'l', 'e', 'l', 'o']

# my_string = str(my_string)
# print(my_string)
# ['h', 'l', 'e', 'l', 'o']

str_ = ''
for i in my_string:
    str_ += i

print(str_)
# hlelo

# I l veoyou
# I l veoyou
# ================================================
my_string = list(my_string)
my_string += my_string[num1]

my_string[num1] = my_string[num2]

my_string[num2] = my_string[len(my_string)-1]

my_string = my_string[:len(my_string)-1]

str_ = ''
for i in my_string:
    str_ += i

print(str_)