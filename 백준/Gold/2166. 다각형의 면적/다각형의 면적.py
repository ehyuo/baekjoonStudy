n = int(input())
x_points = []
y_points = []
for _ in range(n):
    x, y = map(int, input().split())
    x_points.append(x)
    y_points.append(y)

x_points.append(x_points[0])
y_points.append(y_points[0])
areas = []

for i in range(n):
    areas.append((x_points[i]*y_points[i+1])-(x_points[i+1]*y_points[i]))
    
print(round(abs(sum(areas))/2, 1))