#두 점 사이의 거리의 제곱 구하기
def getSquaredLength(coordinate1, coordinate2):
    result = 0
    result += (coordinate1[0]-coordinate2[0])**2
    result += (coordinate1[1]-coordinate2[1])**2
    return result

#정사각형인지 판단
def isSquare(coord1, coord2, coord3, coord4):
    coordinates = [coord1, coord2, coord3, coord4]
    lengths = []
    for i in range(4):
        for j in range(i+1, 4):
            lengths.append(getSquaredLength(coordinates[i], coordinates[j]))
    
    #제일 긴 거리가 제일 짧은 거리의 루트2배
    if max(lengths) == min(lengths) * 2:
        print(1)
    else:
        print(0)
    

t = int(input())
data=[]
for i in range(t*4):
    data.append(list(map(int, input().split())))
    
for i in range(t):
    isSquare(data[i*4], data[i*4+1], data[i*4+2], data[i*4+3])
    
    
    