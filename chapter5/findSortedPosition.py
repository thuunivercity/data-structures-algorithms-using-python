# modified version of the binary search that returns the index with
# a sorted sequence indicating where the target should be located.
def findSortedPosition(theList, target):
    low = 0
    high = len(theList) - 1
    while low <= high:
        mid = (high + low) // 2
        if theList[mid] == target:
            return mid             # Index of the target
        elif target < theList[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return low               # Index where the target value should be
