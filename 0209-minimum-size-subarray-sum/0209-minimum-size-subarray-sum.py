class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        curr_sum = 0
        minLength = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                minLength = min(minLength, right - left + 1)

                curr_sum -= nums[left]
                left += 1

        if minLength == float('inf'):
            return 0

        return minLength