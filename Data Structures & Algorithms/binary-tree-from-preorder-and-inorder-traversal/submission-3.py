# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_indices = {val: idx for idx, val in enumerate(inorder)}

        root_index = 0

        def dfs(inorder_lowerbound, inorder_upperbound):
            nonlocal root_index

            if inorder_lowerbound > inorder_upperbound:
                return None
            
            root = TreeNode(preorder[root_index])
            root_inorder_idx = inorder_indices[root.val]
            root_index += 1

            root.left = dfs(
                inorder_lowerbound,
                root_inorder_idx - 1
            )
            root.right = dfs(
                root_inorder_idx + 1,
                inorder_upperbound
            )

            return root
        
        return dfs(0, len(inorder) - 1)