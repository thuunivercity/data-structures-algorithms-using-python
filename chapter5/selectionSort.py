def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n-1):
         # Assume the ith element is the  smallest
        smallNdx = i
         # Determine if any other element contains a samller value.
        for j in range(i+1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j

         # Swap the ith value and smallNdx value only if the smallest
         # value is not already in its proper position. Some implementation
         # omit testing the condition and always swap the two values.
        theSeq[i], theSeq[smallNdx] = theSeq[smallNdx], theSeq[i]

    return theSeq

# test the sorting method using instance
testlist = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
print testlist
print selectionSort(testlist)
