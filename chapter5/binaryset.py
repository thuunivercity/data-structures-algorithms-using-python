#Implementation of the Set ADT using a sorted list
class Set:
     # Creates an empty set instance
    def __init__(self):
        self._theElements = list()

     # Returns the number of items in the set
    def __len__(self):
        return len(self._theElements)
    
     # Determines if an element is in the set
    def __contains__(self, elements):
    
     # Adds a new unique element to the set
    def add(self, element):
        if element not in self:
            ndx = self._findPosition(element)
            self._theElements.insert(ndx, element)
 
     # Remove an element from the set
    def remove(self, element):
        assert element in self, "The element must be in the set."
        ndx = self._findPosition(element)
        self._theElemetns.pop(ndx)
     
     # Determines if this set is a subset of setB
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True
     
     # The remaining methods go here.
     # ......
     # Return an iterator for traversing the list of items.
    def __iter__(self):
        return _SetIterator(self._theElements)
    
     # Finds the position of the element within the orderd list
    def _findPosition(self, element):
        low = 0
        high = len(theList) - 1
        while low <= high:
            mid = (high + low) / 2
            if theList[mid] == target:
                return mid
            elif target < theList[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

