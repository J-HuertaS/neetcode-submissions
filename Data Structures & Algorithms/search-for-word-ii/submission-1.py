class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        total_words = set()

        def dfs(board,check,word,index,x,y):
            if index >= 10:
                return 

            # si se sale del board, retorna false
            if x < 0 or x >= len(board[0]) or y < 0 or y>= len(board):
                return 

            # si ya se habia recorrido la casilla, retorna false
            if (x,y) in check:
                return 

            check.add((x,y))
            word += board[y][x]
            total_words.add(word)

            # buscar en las 4 direcciones
            dfs(board,check,word,index+1,x+1,y)
            dfs(board,check,word,index+1,x-1,y)
            dfs(board,check,word,index+1,x,y+1)
            dfs(board,check,word,index+1,x,y-1)

            check.remove((x,y))

        
        for i in range(len(board)): # y
            for j in range(len(board[0])): # x
                check = set()
                dfs(board,check,"",0,j,i)

        output = set(words) & total_words

        return list(output)
        