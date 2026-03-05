class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    
    dummy = ListNode(-1)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        
        current = current.next

    # Attach remaining nodes
    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


# -------- Function Call -------- #

# Create list1 : 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Create list2 : 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Call function
merged_head = mergeTwoLists(list1, list2)

# Print merged list
while merged_head:
    print(merged_head.val, end=" ")
    merged_head = merged_head.next