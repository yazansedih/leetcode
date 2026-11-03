from collections import deque

class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                # Last node of this level
                if i == level_size - 1:
                    result.append(node.val)

        return result