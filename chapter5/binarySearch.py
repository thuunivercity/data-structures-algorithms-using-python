def binarySearch( theValues, target ):
    low = 0
    high = len(theValues) - 1
    
    while low <= high:
        mid = (high+low) // 2
        if theValues[mid] == target:
            return True
        elif target < theValues[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return False

