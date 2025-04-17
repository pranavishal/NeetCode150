class Solution:
    def trap(self, height: List[int]) -> int:
        # Prefix Maximum Array
        prefix = [0] * len(height)
        currentPrefixMax = 0
        for i in range(len(height)):
            if currentPrefixMax > height[i]:
                prefix[i] = currentPrefixMax
            else:
                prefix[i] = 0
                currentPrefixMax = height[i]

        # Suffix Maximum Array
        suffix = [0] * len(height)
        currentSuffixMax = 0
        for i in range(len(height) - 1, -1, -1):
            if currentSuffixMax > height[i]:
                suffix[i] = currentSuffixMax
            else:
                suffix[i] = 0
                currentSuffixMax = height[i]

        #Water stored at element i is (min(prefix[i], suffix[i]) - height[i])
        totalArea = 0
        for i in range(len(height)):
            area = min(prefix[i], suffix[i]) - height[i]
            if area > 0:
                totalArea += area
        
        return totalArea





                








