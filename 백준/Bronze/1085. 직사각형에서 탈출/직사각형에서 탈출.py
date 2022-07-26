x, y, w, h = map(int, input().split())

arr1 = [0, 0, w, h]
arr2 = [x, y, x, y]

results = []
for i in range(4):
    results.append(abs(arr1[i]-arr2[i]))
    
print(min(results))