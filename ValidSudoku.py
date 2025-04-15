class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #iterating through each row to ensure all rows are valid
        for row in board:
            valid = set()
            for i in range(len(row)):
                if row[i] in valid and row[i] != ".":
                    print("BAD ROW")
                    return False
                else:
                    valid.add(row[i])
        
        #iterating through each column to ensure all columns are valid
        for i in range(len(board[0])):
            valid = set()
            for j in range(len(board)):
                if board[j][i] in valid and board[j][i] != ".":
                    print("BAD COL")
                    return False
                else:
                    valid.add(board[j][i])
        
        #ensuring all 3x3 squares are valid
        rowEnds = [2, 5, 8]
        colEnds = [2, 5, 8]

        for rowEnd in rowEnds:
            for colEnd in colEnds:
                valid = set()
                for i in range(2, -1, -1):
                    for j in range(2, -1, -1):
                        if board[colEnd - j][rowEnd - i] in valid and board[colEnd - j][rowEnd - i] != ".":
                            print("BAD Square")
                            return False
                        else:
                            valid.add(board[colEnd - j][rowEnd - i])


        # All conditions did not fail, thus board must be valid
        return True
        
        
