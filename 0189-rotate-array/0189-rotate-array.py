class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        nums[:] = nums[-k:] + nums[:-k] 
        # # reverse whole array
        # nums.reverse()

        # # reverse first k elements
        # nums[:k] = reversed(nums[:k])

        # # reverse remaining
        # nums[k:] = reversed(nums[k:])