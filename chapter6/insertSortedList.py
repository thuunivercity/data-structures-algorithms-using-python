# Given the head pointer, insert a value into a sorted linked list.
# Find the insertion point for the new value.

predNode = None
curNode = head
while curNode is not None and value > curNode.data:
    predNode = curNode
    curNode = curNode.next

# Create the new node for the new value.
newNode = ListNode(value)
newNode.next = curNode

# Link the new node for the new value
newNode = ListNode(value)
newNode.next = curNode

# Link the new node into the list
if curNode is head:
    head = newNode
else:
    predNode.next = newNode

