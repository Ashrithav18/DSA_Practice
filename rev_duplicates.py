class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeDuplicates(head):
    
    seen = set()
    curr = head
    prev = None
    
    while curr:
        
        if curr.val in seen:
            # Remove duplicate node
            prev.next = curr.next
        else:
            # First time seeing this value
            seen.add(curr.val)
            prev = curr
        
        curr = curr.next
    
    return head

# Create linked list
head = ListNode(12)
head.next = ListNode(11)
head.next.next = ListNode(12)
head.next.next.next = ListNode(21)
head.next.next.next.next = ListNode(41)
head.next.next.next.next.next = ListNode(43)
head.next.next.next.next.next.next = ListNode(21)

# Call function
head = removeDuplicates(head)

# Print list
temp = head
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next