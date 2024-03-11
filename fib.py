import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

start_time = time.time()
print(fib(40))
end_time = time.time()

# 40번째 수는 대략 2^40 -> 1조번이 넘어감
