N, M = tuple(map(int, input().split()))

graph = [
    [0 for _ in range(N + 1)]
    for _ in range(N + 1)
]

for _ in range(M):
    start_vertex, end_vertex = tuple(map(int, input().split()))
    graph[start_vertex][end_vertex] = 1
    graph[end_vertex][start_vertex] = 1

visited = [False for _ in range(N + 1)]

def dfs(vertex):
    for curr_v in graph[vertex]:
        if graph[vertex][curr_v] and not visited[curr_v]:

            visited[curr_v] = True
            dfs(curr_v)

root_vertex = 1
visited[root_vertex] = True
dfs(root_vertex)

cnt = 1
for elem in visited:
    if elem == True:
        cnt += 1

print(cnt)