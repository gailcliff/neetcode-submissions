# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0

        def dfs(root, max_val_in_path):
            nonlocal good_nodes
            
            if not root:
                return
            
            if root.val >= max_val_in_path:
                good_nodes += 1

            max_val_in_path = max(max_val_in_path, root.val)

            dfs(root.left, max_val_in_path)
            dfs(root.right, max_val_in_path)
        
        dfs(root, root.val)
        return good_nodes