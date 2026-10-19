class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        # Time: O(log n), Space: O(n)
        nums.sort()
        return nums[len(nums) // 2]
        """

        candidate = None
        count = 0

        for num in nums:

            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else:
                count -= 1

        return candidate