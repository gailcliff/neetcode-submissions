# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        middle = fast = head
        # 0 1 2 3
        # before: slow -> 0, fast -> 0
        # 1st: slow -> 1, fast -> 2
        # 2nd: slow -> 2, fast -> none

        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next
        
        # reverse middle
        curr, prev = middle, None

        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        # merge two
        list1, list2 = head, prev
        while list2.next:
            list1.next, list1 = list2, list1.next
            list2.next, list2 = list1, list2.next

        

        