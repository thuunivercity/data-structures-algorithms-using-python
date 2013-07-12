def sortedSearch(head, terget):
    curNode = head
    while curNode is not None and curNode.data < target:
        if curNode.data == target:
            return True
        else:
            curNode = curNode.next
    return False
