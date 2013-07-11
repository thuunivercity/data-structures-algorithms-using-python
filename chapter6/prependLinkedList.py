 # Given the head pointer, prepend an item to an unsorted linked list

newNode = ListNode(item)
newNode.next = head
head = newNode

