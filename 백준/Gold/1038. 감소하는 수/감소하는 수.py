import sys
from itertools import combinations

n = int(sys.stdin.readline())

arr = []
for i in range(1, 11):
    for j in combinations(range(0, 10), i):
        temp = list(j)
        temp.sort(reverse=True)
        arr.append("".join(map(str, temp)))

arr = list(map(int, arr))
arr.sort()
try:
    print(arr[n])
except:
    print(-1)