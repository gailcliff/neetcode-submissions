# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        valid = True

        def dfs(node):
            nonlocal valid

            if not node:
                return float('inf'), float('-inf')
            
            min_left, max_left = dfs(node.left)
            min_right, max_right = dfs(node.right)

            if max_left >= node.val or min_right <= node.val:
                valid = False

            return (min(min_left, min_right, node.val),
                    max(max_left, max_right, node.val))
        
        dfs(root)

        return valid
