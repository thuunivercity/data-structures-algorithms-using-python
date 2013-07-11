# Define a linked list iterator for the Bag ADT
class _BagIterator:
    def __init__(self, listHead):
        self._curNode = listHead
   
    def __iter__(self):
        return self
    
    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item

