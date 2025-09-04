class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        k %= n
        if k == 0:
            return  # already rotated

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        # 1) reverse all
        reverse(0, n - 1)
        # 2) reverse first k
        reverse(0, k - 1)
        # 3) reverse the rest
        reverse(k, n - 1)
