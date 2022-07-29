n, k = map(int, input().split())

arr = []
arr.append([1 for i in range(1, k+1)])
for i in range(1, n+1):
    temp = [1]
    for j in range(1, k):
        temp.append(temp[j-1]+arr[i-1][j])
    arr.append(temp)
    
print(arr[n][k-1]%1000000000)