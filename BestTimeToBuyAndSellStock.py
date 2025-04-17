class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxAmount = 0
        prevMax = prices[0]
        prevMin = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > prevMax:
                newAmount = prices[i] - prevMin
                if newAmount > maxAmount:
                    maxAmount = newAmount
                prevMax = prices[i]
              
            
            if prices[i] < prevMin:
                prevMin = prices[i]
                prevMax = prices[i]

            
        return maxAmount


