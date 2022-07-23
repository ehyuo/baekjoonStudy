#값 입력
n = int(input())
list_n = list(map(int, input().split()))
result = []

for i in range(n, 0, -1):
    p = list_n.pop() 	#리스트의 가장 끝 값
    if i == n:	#가장 키가 큰 사람은 그냥 리스트에 담는다.
    	result.append(i)
    else:	#이후의 사람들은 p 위치에 넣는다.
        result.insert(p, i)

#결과 출력
print(*result)