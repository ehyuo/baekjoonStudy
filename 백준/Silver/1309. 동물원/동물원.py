n = int(input())

if n == 1:
    print(3)
elif n == 2:
    print(7)
else:
    a, b = 3, 7
    for i in range(n-1):
        a, b = b, b*2 + a
    print(a%9901)