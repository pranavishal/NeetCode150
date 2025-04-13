class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            value = target - nums[i]

            if value in numMap:
                return [numMap[value], i]
            
            else:
                if nums[i] not in numMap:
                    numMap[nums[i]] = i
                

        
