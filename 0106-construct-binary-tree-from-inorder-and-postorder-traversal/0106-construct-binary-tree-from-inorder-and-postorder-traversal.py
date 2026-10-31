class Solution(object):
    def buildTree(self, inorder, postorder):

        if not inorder or not postorder:
            return None

        # Last element in postorder is the root
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # Find root position in inorder
        mid = inorder.index(root_val)

        # Build left subtree
        root.left = self.buildTree(
            inorder[:mid],
            postorder[:mid]
        )

        # Build right subtree
        root.right = self.buildTree(
            inorder[mid + 1:],
            postorder[mid:-1]
        )

        return root