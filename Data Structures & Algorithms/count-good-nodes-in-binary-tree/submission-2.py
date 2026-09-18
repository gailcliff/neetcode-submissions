# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val_in_path):
            if not node:
                return 0
            
            good_nodes_for_node = 1 if node.val >= max_val_in_path else 0
            max_val_in_path = max(max_val_in_path, node.val)

            good_nodes_for_node += (dfs(node.left, max_val_in_path) +
            dfs(node.right, max_val_in_path))

            return good_nodes_for_node
        
        return dfs(root, root.val)