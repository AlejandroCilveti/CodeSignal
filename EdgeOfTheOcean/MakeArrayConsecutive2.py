def makeArrayConsecutive2(statues):
    num = min(statues)
    maximum = max(statues)
    finish = False
    needed = 0
    
    while not finish:
        num += 1
        
        if num >= maximum:
            break
            
        try:
            if not num in statues:
                needed += 1
        except:
            needed += 1
            finish = True
    
    return needed
