import math
n = int(input())
arr = list(map(int, input().split()))

def isPrime(n):
    r = math.floor(n**0.5)
    result = True
    for i in range(2, r+1):
        if n % i == 0:
            result = False
            break

    return result

count = 0
for i in arr:
    if i == 1:
        continue
    if i == 2 or i == 3:
        count += 1
    elif isPrime(i):
        count += 1

print(count)