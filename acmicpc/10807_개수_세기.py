N = int(input())

integers = list(map(int, input().split()))

v = int(input())

count = 0
for integer in integers:
    if integer == v:
        count += 1

print(count)