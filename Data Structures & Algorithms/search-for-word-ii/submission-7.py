class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        total_words = set()

        def dfs(board,check,trie_node,x,y,current_word):
            if "*" in trie_node:
                total_words.add(current_word)

            # si se sale del board, retorna false
            if x < 0 or x >= len(board[0]) or y < 0 or y>= len(board):
                return 

            # si ya se habia recorrido la casilla, retorna false
            if (x,y) in check:
                return 

            letra = board[y][x]

            # si no existe en el trie, retorna
            if letra not in trie_node:
                return

            check.add((x,y))        

            # buscar en las 4 direcciones
            aux = trie_node[letra]
            current_word += letra
            dfs(board,check,aux,x+1,y,current_word)
            dfs(board,check,aux,x-1,y,current_word)
            dfs(board,check,aux,x,y+1,current_word)
            dfs(board,check,aux,x,y-1,current_word)

            check.remove((x,y))

        trie = {}

        # construir trie para las palabras
        for word in words:
            trie_node = trie
            for char in word:
                if char not in trie_node:
                    trie_node[char] = {}
                trie_node = trie_node[char]
            trie_node["*"] = True

        for i in range(len(board)): # y
            for j in range(len(board[0])): # x
                check = set()
                dfs(board,check,trie,j,i,"")

        output = set(words) & total_words

        return list(output)
        