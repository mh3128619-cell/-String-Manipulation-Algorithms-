class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

def sortList(head):
    if not head or not head.next:
        return head

    slow, fast = head, head
    temp = None
    while fast and fast.next:
        temp = slow
        slow = slow.next
        fast = fast.next.next
    
    temp.next = None

    left_side = sortList(head)
    right_side = sortList(slow)

    return mergeTwoLists(left_side, right_side)

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))

print("Original list:", end=" ")
print_list(head)

sorted_head = sortList(head)

print("Sorted list:", end=" ")
print_list(sorted_head)

head2 = ListNode(5, ListNode(1, ListNode(3, ListNode(2, ListNode(4, ListNode(0))))))

print("\nOriginal list 2:", end=" ")
print_list(head2)

sorted_head2 = sortList(head2)

print("Sorted list 2:", end=" ")
print_list(sorted_head2)
