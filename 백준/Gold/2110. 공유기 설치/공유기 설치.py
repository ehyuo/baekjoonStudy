import sys

#값 입력
n, c = map(int, sys.stdin.readline().split())
home_pos = []

for i in range(n):
    home_pos.append(int(sys.stdin.readline()))
    
home_pos.sort() #정렬

start = 1 #집 사이의 최소거리
end = home_pos[-1] - home_pos[0] #집 사이의 최대거리
result = 0

#이분 탐색
while start <= end:
    mid = (start + end) // 2
    count = 1  #공유기의 개수
    v = home_pos[0]  #최소 좌표
    for i in home_pos:
        if i >= v + mid:  #mid만큼 거리를 두고 공유기를 설치할 수 있으면 count ++
            v = i
            count += 1
            
    #count가 c보다 크면 조건 성립, 거리 늘림
    if count >= c:
        start = mid + 1
        result = mid
    #아니라면 거리 좁힘
    else:
        end = mid - 1
        
print(result)