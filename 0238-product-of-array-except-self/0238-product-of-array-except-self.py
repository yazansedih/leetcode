class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = 1
        suffix = 1
        answer = [1] * len(nums)

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer