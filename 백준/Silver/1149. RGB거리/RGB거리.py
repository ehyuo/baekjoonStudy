n = int(input())

costs = []
for i in range(n):
    costs.append(list(map(int, input().split())))
    
#점화식
for i in range(1, n):
    costs[i][0] += min(costs[i-1][1], costs[i-1][2]) #i번째 집을 빨강색으로 칠할 때 최소 비용
    costs[i][1] += min(costs[i-1][0], costs[i-1][2]) #i번째 집을 초록색으로 칠할 때 최소 비용
    costs[i][2] += min(costs[i-1][0], costs[i-1][1]) #i번째 집을 파랑색으로 칠할 때 최소 비용
    
print(min(costs[n-1]))
