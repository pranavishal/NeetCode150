class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ## Our recurrence relation is defined as follows
        ## Let matrix M be a matrix where i represents the ith different coin denomination
        ## and j represents the target amount

        ## M[i][j] represents the total distinct combinations of up to and including the 
        ## ith coin, with target amount j

        ## We will define a recurrence relation as follows:
        ## M[i][j] = SUM of i = 1 to floor(j/coins[i]) of M[i - 1][j - i*coins[i]]

        ## Base case: M[0][j] = 1 if j % coins[i] = 0, 0 otherwise
        ## Base case [i][0] = 1 for all i

        j = amount
        i = len(coins)

        M = [[0 for _ in range(j + 1)] for _ in range(i)]

        # Base cases 
        # 
        for x in range(j + 1):
            if x % coins[0] == 0:
                M[0][x] = 1
        
        for x in range(i):
            M[x][0] = 1
        
        for x in range(1, i):
            for y in range(1, j + 1):
                #print(x)
                #print(coins[x])
                #print(y)
                uniqueAmount = y // coins[x]
                #print(uniqueAmount)
                

                for z in range(0, uniqueAmount + 1):
                    if M[x-1][y - (z * coins[x])] == 0:
                        if z * coins[x] == y:
                            M[x][y] += 1
                    else:
                        M[x][y] += M[x-1][y - (z * coins[x])]
                
                
                
        
        
        return M[i-1][j] 


                
            


        
