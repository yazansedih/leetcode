class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        # Build the directed graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def dfs(course):
            # A cycle exists
            if state[course] == 1:
                return False

            # This course was already checked
            if state[course] == 2:
                return True

            # Mark as currently visiting
            state[course] = 1

            # Explore neighboring courses
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            # Mark as completely visited
            state[course] = 2
            return True

        # Check every course, including disconnected components
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True