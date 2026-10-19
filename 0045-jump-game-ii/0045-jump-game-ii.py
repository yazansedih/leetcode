
class Solution(object):
    def jump(self, nums):
        n = len(nums)

        jumps = 0
        max_reach = 0
        current_end = 0

        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = max_reach

        return jumps
