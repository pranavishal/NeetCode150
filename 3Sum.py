class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        totalTriplets = []
        tripletTupleSet = set()
        for i in range(len(nums)):
            numsSet = set()
            for j in range(i + 1, len(nums)):
                target = -nums[i] - nums[j]
                if target in numsSet:
                    tmpTuple = tuple(sorted((nums[i], nums[j], target)))
                    if tmpTuple not in tripletTupleSet:
                        totalTriplets.append([tmpTuple[0], tmpTuple[1], tmpTuple[2]])
                        tripletTupleSet.add(tmpTuple)
                
                if nums[j] not in numsSet:
                    numsSet.add(nums[j])
        

        return totalTriplets
                    
                

                    
        
