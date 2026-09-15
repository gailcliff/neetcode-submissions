# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0

        temp = head
        while temp:
            temp = temp.next
            N += 1
        
        n = N - n

        if n == 0:
            return head.next
        
        curr = head
        for i in range(n-1):
            curr = curr.next

        curr.next = curr.next.next

        return head