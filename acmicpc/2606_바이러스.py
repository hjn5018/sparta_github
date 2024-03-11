import sys

computers = int(sys.stdin.readline())
networks = int(sys.stdin.readline())
connections = [[] for _ in range(computers + 1)]
# sys.stdout.write(f"{connections}")
# [[], [], [], [], [], [], [], []]

visited = [0] * (computers + 1)
# sys.stdout.write(f"{visited}")
# [0, 0, 0, 0, 0, 0, 0, 0]

for _ in range(networks):
    a, b = map(int, sys.stdin.readline().split())
    connections[a] += [b]
    connections[b] += [a]
# connections[1] += [2]
# connections[2] += [1]
# sys.stdout.write(f"{connections}")
# [[], [2], [1], [], [], [], [], []]
    
# connections[1] += [5]
# connections[5] += [1]
# sys.stdout.write(f"{connections}")
# [[], [2, 5], [1], [], [], [1], [], []]

def dfs(computer: int):
    visited[computer] = 1

    coms = connections[computer]
    if len(coms) == 0:
    # if len(coms:= connections[computer]) == 0:
    # 위 두 줄과 같음.
    #Assignment Expression : if 문에서의 새로운 변수 할당 표현식. := 를 사용하면 if 문 내부에서 변수 선언을 해줄 수 있습니다~! (버전 3.8 이상)
        return

    for com in coms:
        if not visited[com]:
            dfs(com)

dfs(1)

sys.stdout.write(f"{sum(visited) -1}")