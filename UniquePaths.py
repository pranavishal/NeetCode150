class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Let P be a matrix where P[i][j] represents i spots to the left and j spots above
        #the bottom right corner

        # Thus, the highest amount of unique paths for spot [i][j] is the numer of unique
        # spots at spot [i-1][j] + [i][j-1]

        P = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, n):
            P[0][i] = 1
        
        for i in range(1, m):
            P[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                P[i][j] = P[i-1][j] + P[i][j-1]
        

        return P[m-1][n-1]

        return 0

        
