def insertionSort(theSeq):
    n = len(theSeq)i
     # Starts with the first item as the only sorted entry.
    for i in range(1, n):
         # Save the value to be positioned.
        value = theSeq[i]
         # Find the position where value fits in the orderd part of the list.
        pos = i - 1
        while pos >= 0 and value < theSeq[pos]:
             # Shift the items to the right during the search
            theSeq[pos+1] = theSeq[pos]
            pos = pos - 1
         # Put the saved value in to the open slot.
        theSeq[pos+1] = value
        print('iteration#{}: {}'.format(i, theSeq))

    return theSeq

#test the insertion sorting method using instance
testlist = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
print('Before insertion sort:'.format(testlist))
print('After insertion sort:'.format(insertionSort(testlist)))
    
