def findSmallest( theValue ):
    n = len( theValues )
    smallest = theValues[0]
    for i in range( 1, n ):
        if theList[i] < smallest :
            smallest = theValues[i]
    return smallest

