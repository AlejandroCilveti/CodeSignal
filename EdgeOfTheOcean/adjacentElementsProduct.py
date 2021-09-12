def adjacentElementsProduct(inputArray):
    highest = -10001
    x = -1
    
    while True:
        x += 1
        try:
            result = inputArray[x] * inputArray[x+1]
            if result >= highest:
                highest = result
        except:
            return highest
