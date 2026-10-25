class Solution(object):
    def insert(self, intervals, newInterval):
        result = []
        start, end = newInterval

        for interval in intervals:
            if interval[1] < start:
                result.append(interval)

            elif interval[0] > end:
                result.append([start, end])
                start, end = interval
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])

        result.append([start, end])

        return result