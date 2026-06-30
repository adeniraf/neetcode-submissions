# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        tail = head
        length = 1

        # Get the length of the linked list, excluding the dummy node
        while tail.next:
            tail = tail.next
            length += 1

        # iterate from the dummy node, while the node to remove is 
        # not the next one, keep going
        # if you find the node to remove is the next node, point curr.next to curr.next.next

        current = 0
        iterator = dummy

        print(dummy)
        print(iterator)
        while current != length - n:
            iterator = iterator.next
            current += 1
        iterator.next = iterator.next.next

        return dummy.next

        