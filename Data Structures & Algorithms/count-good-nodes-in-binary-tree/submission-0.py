# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        
        def dfs(node, node_to_beat):
            nonlocal good_nodes

            if not node:
                return
            
            if node.val >= node_to_beat.val:
                good_nodes += 1
                node_to_beat = node
                print(node.val)
            
            dfs(node.left, node_to_beat) 
            dfs(node.right, node_to_beat)
                    
        dfs(root, root)
        return good_nodes