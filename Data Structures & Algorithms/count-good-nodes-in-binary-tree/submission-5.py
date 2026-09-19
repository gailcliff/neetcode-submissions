# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        
        def dfs(node, max_val_in_path):
            nonlocal good_nodes

            if not node:
                return
            
            good_nodes += (1 if node.val >= max_val_in_path else 0)

            max_val_in_path = max(max_val_in_path, node.val)
            
            dfs(node.left, max_val_in_path) 
            dfs(node.right, max_val_in_path)

        
        dfs(root, root.val)
        return good_nodes