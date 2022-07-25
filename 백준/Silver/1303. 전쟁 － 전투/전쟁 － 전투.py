from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
arr = []

for i in range(m):
    arr.append(list(sys.stdin.readline()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
	t = arr[y][x]
	if t == 0:
		return 0
	count = 0
	queue = deque([[x, y]])
	while queue:
		count += 1
		v = queue.popleft()
		arr[v[1]][v[0]] = 0
		for i in range(4):
			if v[0]+dx[i] <0 or v[1]+dy[i]<0 or v[0]+dx[i] == n or v[1]+dy[i] == m:
				continue
			elif not arr[v[1]+dy[i]][v[0]+dx[i]] == t:
				continue
			else:
				arr[v[1] + dy[i]][v[0] + dx[i]] = 0
				queue.append([v[0] + dx[i], v[1] + dy[i]])
				
	return count

w_count = 0
b_count = 0
for i in range(n):
    for j in range(m):
        if arr[j][i] == "W":
            w_count += bfs(i, j) ** 2
            
        else:
            
            b_count += bfs(i, j) ** 2
            
print(w_count, b_count)
