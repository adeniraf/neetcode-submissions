class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_height = 0

        while left < right:
            current_height = (right - left) * min(heights[right], heights[left])
            max_height = max(current_height, max_height)
            
            # conditions for incrementing/decrementing pointers
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_height
