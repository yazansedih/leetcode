class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        count = 2
        for i in range(2, len(nums)):
            # allow nums[i] if it doesn't create a 3rd duplicate
            if nums[i] != nums[count - 2]:
                nums[count] = nums[i]
                count += 1

        return count


