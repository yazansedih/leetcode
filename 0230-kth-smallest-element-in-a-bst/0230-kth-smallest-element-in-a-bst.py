class Solution(object):
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = None

        def inOrder(node):
            if node is None or self.result is not None:
                return

            inOrder(node.left)

            self.count += 1

            if self.count == k:
                self.result = node.val
                return

            inOrder(node.right)

        inOrder(root)

        return self.result