class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        for num in nums:
            if num not in numDict:
                numDict[num] = 1
            else:
                numDict[num] += 1
        

        sortedKeys = sorted(numDict, key= lambda num: numDict[num])

        return sortedKeys[-k:]
        
