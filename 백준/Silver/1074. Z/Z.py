n, x, y = map(int, input().split())

def getZ(x, y, n):
    start = 0
    end = 2**(n*2)-1
    temp = 2**(n*2)
    while temp > 1:
        l1 = int(temp**0.5)
        l2 = int(temp/4)
        if x<l1/2 and y<l1/2:
            end -= l2 * 3
        elif x>= l1/2 and y<l1/2:
            start += l2
            end -= l2 * 2
            x = x-l1/2
        elif x<l1/2 and y>=l1/2:
            start += l2*2
            end -= l2 
            y = y-l1/2
        else:
            start += l2*3
            x = x-l1/2
            y = y-l1/2
        temp //= 4
    return start

print(getZ(y, x, n))
