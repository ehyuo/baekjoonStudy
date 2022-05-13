#재귀함수로 계산하면 시간 초과가 남
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
    
t = int(input())
data = []
result = []

for i in range(t):
    data.append(int(input()))

#0이 출력되는 횟수와 1이 출력되는 횟수는 피보나치 수열을 이룸
for i in data:
    if i==0:
        result.append([1, 0])
    else:
        result.append([fibonacci(i-1), fibonacci(i)])
    
for i in result:
    print(i[0], i[1])