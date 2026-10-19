
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left numbers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return result
