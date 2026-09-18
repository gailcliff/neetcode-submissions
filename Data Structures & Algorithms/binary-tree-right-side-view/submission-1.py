# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        right_side_view = []

        while queue:
            level_len = len(queue)

            curr_node = None

            for _ in range(level_len):
                curr_node = queue.popleft()

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            if curr_node:
                right_side_view.append(curr_node.val)
        
        return right_side_view