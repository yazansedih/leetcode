class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums)

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k