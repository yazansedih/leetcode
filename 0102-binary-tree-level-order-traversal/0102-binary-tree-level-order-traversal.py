from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result