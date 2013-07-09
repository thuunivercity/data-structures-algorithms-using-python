def sorteLinearSearch( theValues, item):
    n = len( theValues )
    for i in range( n ):
        if theValues[i] == item :
            return True
        elif theValues[i] > item :
            return False
    return False

