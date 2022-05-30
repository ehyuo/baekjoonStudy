n = list(map(int, input()))
n.sort(reverse=True)
result = 0
for i in range(len(n), 0, -1):
    result += 10**(i-1)*n[len(n)-i]
    
print(result)