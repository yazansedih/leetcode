class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current container area
            width = right - left
            current_area = width * min(height[left], height[right])

            # Update the maximum area
            max_area = max(max_area, current_area)

            # Move the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area