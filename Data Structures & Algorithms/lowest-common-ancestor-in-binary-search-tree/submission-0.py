# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # If we reach the end, there is nothing here.
        if not root:
            return None

        # If we find p or q, return that node upward.
        if root == p or root == q:
            return root

        # Search both subtrees.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q were found in different subtrees,
        # the current node is their lowest common ancestor.
        if left and right:
            return root

        # Otherwise, both nodes are on the same side.
        # Return whichever side found p or q.
        return left if left else right