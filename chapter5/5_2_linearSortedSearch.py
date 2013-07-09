def sorteLinearSearch( theValue, item):
    n = len( theValue )
    for i in range( n ):
        if theValue[i] == item :
            return True
        elif theValue[i] > item :
            return False
    return False

