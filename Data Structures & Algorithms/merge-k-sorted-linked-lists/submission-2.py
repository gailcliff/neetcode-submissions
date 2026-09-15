# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, list1, list2):

        dummy = head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        
        head.next = list1 or list2

        return dummy.next


    def divide_and_merge(self, lists, left, right):
        if left == right:
            return lists[left]
        
        mid = (left + right) // 2

        left = self.divide_and_merge(lists, left, mid)
        right = self.divide_and_merge(lists, mid + 1, right)

        return self.merge(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        return self.divide_and_merge(lists, 0, len(lists) - 1)
        