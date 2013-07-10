#The author made a mistake, and I modify it. Pls check it carfully.

# Sorted a sequence in ascending order using the buble sort algoithm.
def bubbleSort(theSeq):
    n = len(theSeq)
     # Perform n-1 bubble operations on the sequence
    for i in range(n-1):
         # Bubble the largest item to the end
        for j in range(n-1-i):
            if theSeq[j] > theSeq[j+1]:
                 # Swap the j and j+1 items
                theSeq[j], theSeq[j+1] = theSeq[j+1], theSeq[j]
            print('iteration #{}: {}'.format(i, theSeq))

    return theSeq
#test bubble sort using test instance

testlist = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
print('Before bubble sort:{}'.format(testlist))
print('After bubble sort:{}'.format(bubbleSort(testlist)))
