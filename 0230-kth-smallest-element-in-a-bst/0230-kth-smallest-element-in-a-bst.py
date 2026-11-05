class Solution(object):
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return

            inorder(node.left)

            self.count += 1

            if self.count == k:
                self.result = node.val
                return

            inorder(node.right)

        inorder(root)

        return self.result