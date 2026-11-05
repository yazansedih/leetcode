class Solution(object):
    def getMinimumDifference(self, root):
        self.prev = None
        self.min_diff = float('inf')

        def bst(node):
            if node is None:
                return

            bst(node.left)

            if self.prev is not None:
                self.min_diff = min(
                    self.min_diff,
                    node.val - self.prev
                )

            self.prev = node.val

            bst(node.right)

        bst(root)

        return self.min_diff