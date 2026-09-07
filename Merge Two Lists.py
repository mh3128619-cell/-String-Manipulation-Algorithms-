class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next

list1 = ListNode(1, ListNode(2, ListNode(4)))

list2 = ListNode(1, ListNode(3, ListNode(4)))

print("List 1:", end=" ")
current = list1
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

print("List 2:", end=" ")
current = list2
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

merged_list = mergeTwoLists(list1, list2)

print("Merged List:", end=" ")
current = merged_list
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

list3 = ListNode(5)
list4 = ListNode(1, ListNode(2, ListNode(4)))

print("\nList 3:", end=" ")
current = list3
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

print("List 4:", end=" ")
current = list4
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

merged_list_2 = mergeTwoLists(list3, list4)

print("Merged List 2:", end=" ")
current = merged_list_2
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
