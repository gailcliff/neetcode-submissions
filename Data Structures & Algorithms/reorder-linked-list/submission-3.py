# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # first: find middle
        middle, fast = head, head
        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next
        

        # second: reverse secone half (starting from middle)
        curr, prev = middle, None
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        
        # third: merge two halves
        first, second = head, prev
        while second.next:
            first_next = first.next
            first.next = second
            first = first_next

            second_next = second.next
            second.next = first
            second = second_next