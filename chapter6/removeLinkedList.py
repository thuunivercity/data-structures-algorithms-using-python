# Given the head reference, remove a target from a linked list.
predNode = None
curNode = head
while curNode is not None and curNode.data != target:
    predNode = curNode
    curNode = curNode.next

if curNode is not None:
    if curNode is head:
        head = curNode.next
    else:  
        predNode.next = curNode.next

