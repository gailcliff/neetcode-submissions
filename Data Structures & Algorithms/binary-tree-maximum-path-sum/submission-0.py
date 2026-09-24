# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')

        def dfs(node):
            nonlocal max_path_sum

            if not node:
                return 0
            
            left_contrib = max(0, dfs(node.left))
            right_contrib = max(0, dfs(node.right))

            contrib_thru_node = left_contrib + node.val + right_contrib

            max_path_sum = max(max_path_sum, contrib_thru_node)

            # have to choose the best path that goes through this node
            return node.val + max(left_contrib, right_contrib)
        
        dfs(root)
        return max_path_sum
