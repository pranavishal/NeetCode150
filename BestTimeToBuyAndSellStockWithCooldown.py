class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## What is your max profit on day n?
        ## 2 states:
        ## 1. Assume I am holding on Day n
        ## 2. Assume I am not holding on Day n

        ## If we are holding we either bought on day n, or just held from the day before
        ## if we bought on day n, we had to have sold earliest 2 days before

        # If we are not holding
        # If we sold, we either sold today, or  max we didn't do anything from selling a previous day 

        # Consider matrix M[j][n], where n represents the day, and j represents whether you 
        # hold a neetcoin or not. M[j][n] represents the max amount of money you can make 
        # on day n for whether or not you are holding a coin

        # M[0][0] = 0
        # M[1][0] = -p[0]

        M = [[0 for _ in range(len(prices))] for _ in range(2)]
        M[0][0] = 0
        M[1][0] = -prices[0]

        n = len(prices)

        for i in range(1, n):
            M[0][i] = max(M[1][i-1] + prices[i], M[0][i-1])
            if i == 1:
                M[1][i] = max(M[1][i-1], -prices[i])
            else:
                M[1][i] = max(M[1][i-1], M[0][i - 2] - prices[i])
        
        return max(M[0][n-1], M[1][n-1])
        
