class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points.sort(key=lambda x: x[1])
        # [[1,6], [2,8], [10,16], [7,12]]

        arrows = 1
        arrow = points[0][1]

        for start, end in points[1:]:
            if start > arrow:
                arrows += 1
                arrow = end

        return arrows