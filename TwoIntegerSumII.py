class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        beginIndex = 0
        endIndex = len(numbers) - 1

        while beginIndex < endIndex:
            total = numbers[beginIndex] + numbers[endIndex]
            if total == target:
                return [beginIndex + 1, endIndex + 1]
            
            elif total < target:
                beginIndex += 1
            
            else:
                endIndex -= 1
