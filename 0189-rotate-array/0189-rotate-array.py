class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return nums

        # avoid loops
        k = k % len(nums) 

        mid = len(nums) - k

        nums[:] = nums[mid:] + nums[:mid]

        return nums
        