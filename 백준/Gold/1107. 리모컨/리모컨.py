#값 입력
n = int(input())
m = int(input())
if m == 0:
    btn = []
else:
	btn = list(map(int, input().split()))

#고장난 버튼 리스트
list_btn = list(map(str, btn))

#100에서 +, -로만 조작했을 때
min_count = abs(100-n)

for i in range(1000001):
    valid = True
    temp = list(str(i))
    #숫자에 고장난 버튼이 포함되어 있을 경우 break
    for j in temp:
        if j in list_btn:
            valid = False
            break
    
    #값이 유효하다면 버튼 누르는 횟수 계산
    if valid:
        numLength = len(temp)
        temp = int("".join(temp))
        if abs(temp - n) + numLength  < min_count:
            min_count = abs(temp - n) + numLength
            
#최소 횟수 출력
print(min_count)        