# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1: find the middle
        middle, fast = head, head

        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next

        # 0 1 2 3 4
        # before: 1st -> 0, 2nd -> 0
        # it1: 1st -> 1, 2nd -> 2
        # it2: 1st -> 2, 2nd -> 4

        # 2: reverse middle
        curr, prev = middle, None
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        # 0 -> 1 -> 2-> None
        # 4 -> 3 -> 2 ->None

        # 3: merge the two halves
        # both halves share a duplicate node (the last node before None),
        # so we have to do a trick and stop when the second half is at
        # the second-to-last position from the back
        first, second = head, prev
        while second.next:
            first_next = first.next

            first.next = second # it1: 0, 4. it2: 0, 4, 1
            first = first_next # it1: first points to 1. it2: first points to 2

            second_next = second.next
            second.next = first # it1: 0, 4, 1

            second = second_next # it1: second points to 3

