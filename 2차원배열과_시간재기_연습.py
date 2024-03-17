import time

start_time = time.time()

h = []
for i in range(5):
    list_ = []
    for j in range(3):
        list_.append(j)
    h.append(list_)

print(h)

end_time = time.time()
print(f'time : {end_time - start_time}')