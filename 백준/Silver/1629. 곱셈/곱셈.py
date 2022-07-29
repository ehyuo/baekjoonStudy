a, b, c = map(int, input().split())
if a>= c:
    a %= c
count = []
while b>1:
    if b%2 == 0:
        a = a**2 % c
        b //= 2
    else:
        count.append(a)
        b -= 1

m = 1
for i in count:
    m *= i
print(a * m % c)
            