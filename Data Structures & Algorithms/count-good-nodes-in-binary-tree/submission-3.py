# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        queue = deque([(root, root.val)])
        good_nodes = 0

        while queue:
            node, max_val_for_path = queue.pop()

            if node.val >= max_val_for_path:
                good_nodes += 1
                max_val_for_path = node.val
            
            if node.left:
                queue.append((node.left, max_val_for_path))
            if node.right:
                queue.append((node.right, max_val_for_path))
        
        return good_nodes