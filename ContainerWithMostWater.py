class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            minHeight = min(heights[left], heights[right])
            area = minHeight * (right - left)
            if area > maxArea:
                maxArea = area
            
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            
            else:
                left += 1
                right -= 1
        
        return maxArea
