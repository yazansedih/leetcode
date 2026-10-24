class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            complment = target - nums[i]

            if complment in seen:
                return [seen[complment], i]

            seen[nums[i]] = i

        return seen