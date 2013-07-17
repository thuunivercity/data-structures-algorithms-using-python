class SparseMatrix:

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() = self.numRows() and \
            rhsMatrix.numCols() = self.numCols(), \
            "Matrix sizes not compatible for th eadd operation."

    # Create the new matrix
    newMatrix = SparseMatrix(self.numRows(), self.numCols())
    
    # Duplicate the lhs matrix, The elements are mutable, thus we must 
    # create new objects and not simply copy the references.
    
    for element in self._elementList:
        dupElement = _MatrixElement(element.row, element.col, element.value)
        newMatrix._elementList.append(dupElement)
        
    # Iterate through each non-zero element of the rhsMatrix
    for element in rhsMatrix._elementList:
    # Get the value of the corresponding element in the new matrix
        value = newMatrix[element.row, element.col]
        value += element.value
        
        # Store the new value back to the new matrix
        newMatrix[element.row, element.col] = value
        
    # Return the new matrix
    return newMatrix


