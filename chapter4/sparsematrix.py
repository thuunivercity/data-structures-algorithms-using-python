class SparseMatrix:
    # Create a sparse matrix of size numRows x numCols initialised to 0.
    def __init__(self, numRows, numCols):
        self._numRows = numRows
        self._numCols = numCols
        self._elementList = list()

    # Return the number of rows in the matrix
    def numRows(self):
        return self._numRows
    
    # Return the number of colums in the matrix
    def numCols(self):
        return self._numCols
    
    # Return the value of element (i,j): s[i,j]
    def __getitem__(self, ndxTuple):
        pass
    
    # Set the value of element(i,j) to the value s: x[i,j]=s
    def __setitem__(self, ndxTuple, scalar):
        ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
        if ndx is not None:
            if scalar != 0.0:
                self._elementList[ndx].value = scalar
            else:
                self._elementList.pop(ndx)
        else:
            if scalar != 0.0
                element = _MatrixElement(ndxTuple[0], ndxTuple[1], scalar)
                self._elementList.append(element)
    
    # Scale the matrix by the given scalar
    def scaleBy(self, scalar):
        for element in self._elementList:
            element.value *= scalar
    # The additional methods should be placed here...
    # def __add__(self, rhsMatrix):
    # def __sub__(self, rhsMatrix):
    # def __sub__(self, rhsMatrix):
  
    # Helper method used to find a specific matrix element (row, col) in the 
    # list of non-zero entries. None is returned if the element is not found.
    
    def _findPosition(self, row, col):
        n = len(self._elementList):
        for i in range(n):
            if row == self._elementList[i].row and \
                col == self._elelmentList[i].col:
                return i
        return None


    # Storage class for holding the non-zero matrix elements.
    class _MatrixElement:
        def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

            
