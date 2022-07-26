arr = list(map(int, input().split()))
result = ""
if arr[0] == 1:
    result = "ascending"
elif arr[0] == 8:
    result = "descending"
else:
    result = "mixed"

if not result == "mixed":
    b = False
    for i in range(len(arr)-1):
        if not abs(arr[i] - arr[i+1]) == 1:
            b = True
            break
    if b:
        result = "mixed"
        
print(result)
    