class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0
        right = len(nums) - 1

        while left < right:
            if target == nums[left] + nums[right]:
                return [left + 1, right + 1]

            elif target > nums[left] + nums[right]:
                left += 1

            else: 
                right -= 1

        return []