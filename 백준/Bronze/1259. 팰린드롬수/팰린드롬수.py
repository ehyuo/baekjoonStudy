while True:
    n = list(input())
    if n[0] == "0":
        break
    valid = True
    for i in range(len(n)//2):
        if not n[i] == n[len(n)-1-i]:
            valid = False
            break
    if valid:
        print("yes")
    else:
        print("no")
