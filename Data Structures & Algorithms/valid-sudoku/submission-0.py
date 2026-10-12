class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validateColumn(idx):
            flag = set()
            for i in range(9):
                if board[i][idx] != '.':
                    if board[i][idx] in flag:
                        return False
                    flag.add(board[i][idx])

            return True

        def validateRow(idx):
            flag = set()
            for i in range(9):
                if board[idx][i] != '.':
                    if board[idx][i] in flag:
                        return False
                    flag.add(board[idx][i])

            return True
        
        def validateBox(x,y):
            flag = set()
            for i in range(y,y+3):
                for j in range(x,x+3):
                    if board[i][j] != '.':
                        if board[i][j] in flag:
                            return False
                        flag.add(board[i][j])

            return True

        for i in range(9):
            if not validateColumn(i) or not validateRow(i):
                return False


        for i in range(0,9,3):
            for j in range(0,9,3):
                if not validateBox(i,j):
                    return False

        return True
