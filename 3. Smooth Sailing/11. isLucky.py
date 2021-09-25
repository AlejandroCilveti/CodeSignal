def isLucky(n):
    n = list(str(n))
    n1 = 0
    n2 = 0
    
    for x in range(int(len(n)/2)):
        n1 += int(n[x])
    
    for x in range(int(len(n)/2), int(len(n))):
        n2 += int(n[x])

    if n1 == n2:
        return True
    else:
        return False
