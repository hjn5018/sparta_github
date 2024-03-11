N = int(input())

scores = list(map(int, input().split()))

max_score = max(scores)

# forged_score = [x/max_score*100 for x in scores]

forged_score = []
for i in scores:
    forged_score.append(i / max_score * 100)

# print(forged_score)
# [50.0, 100.0, 75.0]
    
sum = 0
for score in forged_score:
    sum += score

avg = sum / len(forged_score)

print(avg)