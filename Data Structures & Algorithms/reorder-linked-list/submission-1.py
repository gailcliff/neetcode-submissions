# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: find the end of the first half
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: split the list into two halves
        second = slow.next
        slow.next = None

        # Step 3: reverse the second half
        curr, prev = second, None

        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        # Step 4: merge the first half and reversed second half
        list1, list2 = head, prev

        while list2:
            list1_next = list1.next
            list2_next = list2.next

            list1.next = list2
            list2.next = list1_next

            list1 = list1_next
            list2 = list2_next