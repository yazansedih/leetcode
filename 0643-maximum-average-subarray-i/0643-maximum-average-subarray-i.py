class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right - k]
            max_sum = max(max_sum, window_sum)
        
        max_avg = max_sum / k

        return max_avg
        
