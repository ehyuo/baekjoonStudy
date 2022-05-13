n, m = map(int, input().split())
data=[]
for i in range(n):
    data.append(list(map(int, input())))

result = 1
for length in range(1, n): #정사각형 한 변의 길이
    for i in range(n-length):
        for j in range(m-length):
            #네 꼭짓점의 값이 같으면 됨
            if data[i][j] == data[i+length][j] == data[i][j+length] == data[i+length][j+length]:
                result = length + 1
                
print(result**2)
