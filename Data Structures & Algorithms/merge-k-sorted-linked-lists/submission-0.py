# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def merge_two(self, list1, list2) -> ListNode:

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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            a, b = lists.pop(), lists.pop()
            merged = self.merge_two(a, b)
            lists.append(merged)
        
        return lists[0]
        