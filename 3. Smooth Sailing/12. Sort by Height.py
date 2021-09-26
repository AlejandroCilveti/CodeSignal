def sortByHeight(a):
    n = []
    for i in range(0, len(a)):
        if a[i] == -1:
            n.append(i)
    
    for i in range(0, len(a)):
        try:
                a.remove(-1)
        except:
            pass

    a = sorted(a)

    for i in range(0, len(n)):
        a.insert(n[i], -1)
    
    return a
