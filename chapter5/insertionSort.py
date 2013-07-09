def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1, n):
        value = theSeq[i]
        pos = i - 1
        while pos >= 0 and value < theSeq[pos]:
            theSeq[pos+1] = theSeq[pos]
            pos = pos - 1
        theSeq[pos+1] = value
    return theSeq

#test the insertion sorting method using instance
testlist = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
print testlist
print insertionSort(testlist)
    
