l = int(input())
s = list(map(int, input().split()))
n = int(input())

#배열 오름차순으로 정리
s.sort()

#n이 속해있는 구간
startNum = 0 
endNum = 0

#n이 속해있는 구간 구하기
for i in range(len(s)):
    if n<s[i]:
        if i==0:
            startNum=0
        else:
            startNum=s[i-1]
        endNum=s[i]
        break

print(0 if (n-startNum)*(endNum-n)==0 else (n-startNum)*(endNum-n)-1)