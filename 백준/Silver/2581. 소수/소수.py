n = int(input())
m = int(input())

arr = [i for i in range(n, m+1)]
last = arr[-1]
result = []
    
for i in arr:
	isPrime = True
	for j in range(2, int(last**0.5) + 1):
		if not i == j and i % j == 0:
			isPrime = False
	if isPrime and not i == 1:
		result.append(i)
        
        
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
