# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def root_to_leaf(node, current_number):

            if node is None:
                return 0

            # Build the current number
            current_number = current_number * 10 + node.val

            # Check if leaf node
            if node.left is None and node.right is None:
                return current_number

            # Traverse left and right subtrees
            left_sum = root_to_leaf(node.left, current_number)
            right_sum = root_to_leaf(node.right, current_number)

            return left_sum + right_sum

        return root_to_leaf(root, 0)