class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def sort012(head):
    
    count = [0, 0, 0]   # count of 0,1,2
    
    temp = head
    
    # Step 1: Count 0s,1s,2s
    while temp:
        count[temp.val] += 1
        temp = temp.next
    
    # Step 2: Rewrite values
    temp = head
    i = 0
    
    while temp:
        
        if count[i] == 0:
            i += 1
        else:
            temp.val = i
            count[i] -= 1
            temp = temp.next
    
    return head
# Create linked list
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(0)
head.next.next.next.next = ListNode(2)
head.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next = ListNode(1)

head = sort012(head)

# Print list
temp = head
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next