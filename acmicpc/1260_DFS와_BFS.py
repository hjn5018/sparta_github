N, M, V = map(int, input().split())


# graph = [0] * N
# print(graph)
# [0, 0, 0, 0]

graph = []
for i in range(N):
    graph.append([])
print(graph)

# [] += [1]
# ->
# [1]
# append
# ->
# [[1]]
# [[], [], [], []]

# [[],[],[]]


# print([[] for x in range(N)])

# for i in range(1,M+1):
#     a, b = map(int, input().split())
#     if i == a:
#         graph[i]


# edge_lists = []
# for _ in range(M):
#     E = list(map(int, input().split()))
    # edge_lists.append(E)
# print(edge_lists)
# [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]


visited = []
def dfs(V):
    visited += [V]


    # pass

    # 탈출


    # 구조
    # dfs()



"".join