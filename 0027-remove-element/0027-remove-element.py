class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)

        i = k = 0
        
        while i < n:
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

            i += 1

        return k