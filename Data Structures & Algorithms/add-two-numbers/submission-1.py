# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        mul = 1
        
        num1, num2 = 0, 0
        
        curr = l1
        while curr:
            num1 += curr.val * mul
            mul *= 10
            curr = curr.next
        
        mul = 1
        curr = l2
        while curr:
            num2 += curr.val * mul
            mul *= 10
            curr = curr.next
        
        num = num1 + num2
        
        if num == 0:
            return ListNode(0)

        dummy = head = ListNode()
        while num > 0:
            digit = num % 10
            head.next = ListNode(digit)
            head = head.next
            num = num // 10
        
        return dummy.next
