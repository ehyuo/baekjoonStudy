from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(graph, start):
	num = [0 for _ in range(n+1)]
	visited = [start]    
	queue = deque([start])
	while queue:
		v = queue.popleft()
		for i in graph[v]:
			if i not in visited:
				num[i] = num[v] + 1
				visited.append(i)
				queue.append(i)
    
	return sum(num)
                
s = []
for i in range(1, n+1):
    s.append(bfs(graph, i))

print(s.index(min(s))+1)