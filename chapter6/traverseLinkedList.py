 # Traversal the linked list
def traversal(head):
    curNode = head
    while curNode is not None:
        print curNode.data
        curNode = curNode.next
