class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentMap = {}

        maxLength = 0

        beginningIndex = 0
        endingIndex = 0

        for i in range(len(s)):
            if s[i] not in currentMap or currentMap[s[i]] < beginningIndex:
                currentMap[s[i]] = i
                length = i - beginningIndex + 1
                if length > maxLength:
                    maxLength = length
            
            else:
                beginningIndex = currentMap[s[i]] + 1
                currentMap[s[i]] = i
        
        return maxLength

                

        
