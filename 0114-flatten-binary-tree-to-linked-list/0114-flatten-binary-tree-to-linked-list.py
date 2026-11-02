# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):

        if root is None:
            return

        # Save the original right subtree
        right_subtree = root.right

        # Move the left subtree to the right
        root.right = root.left
        root.left = None

        # Find the last node in the right chain
        current = root.right

        while current and current.right:
            current = current.right

        # Attach the original right subtree
        if current:
            current.right = right_subtree
        else:
            root.right = right_subtree

        # Recursively flatten the remaining tree
        self.flatten(root.right)