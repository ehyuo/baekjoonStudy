from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#상하좌우로 1을 찾으면 0으로 바꿈
def bfs(data, x, y, m, n):
    queue = deque()
    if data[x][y] == 1:
        data[x][y] = 0
        queue.append([x, y])
        while queue:
            v = queue.popleft()
            for i in range(4):
                nx = v[0]+dx[i]
                ny = v[1]+dy[i]
                if nx < 0 or ny < 0 or nx == m or ny == n:
                    continue
                if data[nx][ny] == 1:
                    data[nx][ny] = 0
                    queue.append([nx, ny])
        return 1     
    else:
        return 0
            
    
t = int(input())
mnk = []
fields = []

#테스트 케이스 입력받기
for i in range(t):
    m, n, k = map(int, input().split())
    mnk.append([m, n, k])
    
    temp = [[0] * n for j in range(m)]
    for j in range(k):
        x, y = map(int, input().split())    
        temp[x][y] = 1
    fields.append(temp)
    
results = []
result = 0
for i in range(t):
    for j in range(mnk[i][0]):    #range(m)
        for k in range(mnk[i][1]):    #range(n)
            if bfs(fields[i], j, k, mnk[i][0], mnk[i][1]) == 1:
                result += 1
    results.append(result)
    result = 0
    
#출력
for i in results:
    print(i)