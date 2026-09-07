class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMiddle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
middle1 = findMiddle(head1)
print(f"Middle of 1 -> 2 -> 3 -> 4 -> 5 is: {middle1.val}")

head2 = ListNode(10, ListNode(20, ListNode(30, ListNode(40))))
middle2 = findMiddle(head2)
print(f"Middle of 10 -> 20 -> 30 -> 40 is: {middle2.val}")

head3 = ListNode(100)
middle3 = findMiddle(head3)
print(f"Middle of 100 is: {middle3.val}")

head4 = None
middle4 = findMiddle(head4)
print(f"Middle of an empty list is: {middle4}")
