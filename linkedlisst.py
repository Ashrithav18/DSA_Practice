class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# -------- Function Call -------- #

# Creating nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Creating cycle (tail connects to node2)
node4.next = node2

# Calling the function
print(hasCycle(node1))