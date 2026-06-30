class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_height = 0
        for i in range(0, len(heights) - 1):
            for j in range(i+1, len(heights)):
                current_height = (j - i) * min(heights[i], heights[j])
                max_height = max(current_height, max_height)

        return max_height