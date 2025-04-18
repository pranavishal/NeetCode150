class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        maxFreqCount = 0
        maxFreqLetter = None 

        beginningIndex = 0

        maxLength = 0

        for i in range(len(s)):
            if s[i] not in freqMap:
                freqMap[s[i]] = 1

            else:
                freqMap[s[i]] += 1
            
            if freqMap[s[i]] > maxFreqCount:
                maxFreqCount = freqMap[s[i]]
                maxFreqLetter = s[i]
            
            replacements = (i - beginningIndex + 1) - maxFreqCount

            if replacements <= k and (i - beginningIndex + 1) > maxLength:
                maxLength = (i - beginningIndex + 1)
            
            elif replacements > k:
                freqMap[s[beginningIndex]] -= 1
                beginningIndex += 1
        
        return maxLength
            


        
