class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                if k >= i - seen[nums[i]]:
                    return True

            seen[nums[i]] = i 

        return False