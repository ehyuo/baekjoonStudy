from collections import deque

#재귀함수를 이용한 dfs
def dfs(graph, v, visited=[]):
    visited.append(v)
    for i in graph[v]:
        if i not in visited:
            dfs(graph, i, visited)
    return visited

#큐를 이용한 bfs
def bfs(graph, v, visited=[]):
    queue = deque([v])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited
            
            
n, m, v = map(int, input().split())
data = []
sortedData=[[] for i in range(n+1)]
visited = [0 for i in range(n)]
for i in range(m):
    data.append(list(map(int, input().split())))

#sortedData[노드의 값] == [노드에 연결된 다른 노드들] 이 되도록 정렬
for i in range(1, n+1):
    for j in data:
        if j[0] == i:
            sortedData[i].append(j[1])
        elif j[1] == i:
            sortedData[i].append(j[0])

#오름차순으로 정렬
for i in sortedData:
    i.sort()
    

#출력
for i in dfs(sortedData, v):
    print(i, end=' ')
print("\n", end='')
for i in bfs(sortedData, v):
    print(i, end=' ')