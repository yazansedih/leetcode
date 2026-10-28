class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()

        result = [intervals[0]]

        for interval in intervals:
            last = result[-1]

            if last[1] >= interval[0]:
                last[1] = max(last[1], interval[1])
            else:
                result.append(interval)

        return result

        
        