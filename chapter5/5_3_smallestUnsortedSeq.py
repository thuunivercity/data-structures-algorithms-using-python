def findSmallest( theValue ):
    n = len( theValue )
    smallest = theValue[0]
    for i in range( 1, n ):
        if theList[i] < smallest :
            smallest = theValue[i]
    return smallest

