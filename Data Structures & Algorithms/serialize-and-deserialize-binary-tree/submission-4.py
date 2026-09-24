# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        preorder = []

        def dfs(node):
            if not node:
                preorder.append('N')
                return
            
            preorder.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return ','.join(preorder)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        preorder = data.split(',')
        root_index = 0

        def dfs() -> Optional[TreeNode]:
            nonlocal root_index

            if preorder[root_index] == 'N':
                root_index += 1
                return None
            
            root = TreeNode(int(preorder[root_index]))
            root_index += 1

            root.left = dfs()
            root.right = dfs()

            return root
        
        root_node = dfs()

        return root_node

