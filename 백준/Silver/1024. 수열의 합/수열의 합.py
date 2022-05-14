n, l = map(int, input().split())
result = []
while True:
    #l이 짝수일 때 ~~ 조건을 충족하면 공차가 1인 등차수열을 만들 수 있음
    if l%2 == 0 and n%(l/2) == 0 and n/(l/2) >= l/2 and n/(l/2) % 2 == 1:
        for i in range(l//2):
            result.append(n/l+0.5+i)
            result.append(n/l-0.5-i)
        break
    #l이 홀수일 때 ~~ 조건을 충족하면 공차가 1인 등차수열을 만들 수 있음
    if l%2 == 1 and n%l == 0 and n/l >= (l-1)/2:
        result.append(n/l)
        for i in range(1, (l+1)//2):
            result.append(n/l+i)
            result.append(n/l-i)
        break
    l += 1
    if n<l*(l-1)/2:
        break
        
result = list(map(int, result))
result.sort()

if len(result) == 0 or len (result) > 100:
    print(-1)
else:
    for i in result:
        print(i, end=' ')