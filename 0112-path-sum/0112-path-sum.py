# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if root is None:
            return False

        # We reached a leaf
        if root.left is None and root.right is None:
            return root.val == targetSum

        targetSum -= root.val

        return(
            self.hasPathSum(root.left, targetSum) or
            self.hasPathSum(root.right, targetSum)
        )
        