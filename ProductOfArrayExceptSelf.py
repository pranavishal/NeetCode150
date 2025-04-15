class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        forwardList = []
        forwardVal = 1
        backwardsList = []
        backwardsVal = 1

        j = len(nums) - 1

        for i in range(len(nums)):
            forwardVal *= nums[i]
            backwardsVal *= nums[j]
            forwardList.append(forwardVal)
            backwardsList.append(backwardsVal)
            j -= 1
        
        output = []

        j = len(nums) - 1
        for i in range(len(nums)):
            if i == 0:
                output.append(backwardsList[j - 1])
            elif i == len(nums) - 1:
                output.append(forwardList[i - 1])
            else:
                appendVal = forwardList[i - 1] * backwardsList[j - 1]
                output.append(appendVal)
            j -= 1
        
        return output
            


        
        
