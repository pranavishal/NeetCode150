class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        startingSeq = set()
        numSet = set()

        for num in nums:
            numSet.add(num)
        
        for num in nums:
            if num - 1 not in numSet:
                startingSeq.add(num)

        maxSeqLength = 1
        currentSeqLength = 0

        for num in startingSeq:
            seq = num
            while seq in numSet:
                currentSeqLength += 1
                if currentSeqLength > maxSeqLength:
                    maxSeqLength = currentSeqLength
                seq += 1
            
            currentSeqLength = 0

        return maxSeqLength

        
            
