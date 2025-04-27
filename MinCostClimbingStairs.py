class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Let's call the minimum cost of the nth step M(n)
        # recurrance relation = min{M(n-1) + C(n-1), M(n - 2) + C(n - 2)}

        n = len(cost)

        minCost = [0] * (n + 1)

        minCost[0] = 0
        minCost[1] = 0

        for i in range(2, n + 1):
            minCost[i] = min(minCost[i - 1] + cost[i - 1], minCost[i - 2] + cost[i - 2])
        
        return minCost[n]
