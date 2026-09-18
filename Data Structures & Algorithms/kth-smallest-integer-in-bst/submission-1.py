# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = None

        def dfs_inorder(node): 
            nonlocal count, res

            if not node:
                return
            
            dfs_inorder(node.left)
            if count == 0:
                return

            count -= 1

            if count == 0:
                res = node.val
                return

            dfs_inorder(node.right)

        dfs_inorder(root)

        return res
