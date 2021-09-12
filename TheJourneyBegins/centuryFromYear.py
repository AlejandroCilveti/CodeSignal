def centuryFromYear(year):
    
    minYear = -101
    maxYear = 0
    century = 0
    
    while True:
        minYear += 100
        maxYear += 100
        century += 1
    
        if year >= minYear and year <= maxYear:
            return century   
