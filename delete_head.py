class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


# Create list
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(4)
head.next.next.next = ListNode(30)

# Node to delete (20)
delNode = head.next

# Call function
deleteNode(delNode)

# Print list
temp = head
while temp:
    print(temp.val, end=" ")
    temp = temp.next