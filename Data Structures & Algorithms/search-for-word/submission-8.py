class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x = y = 0
        check = set()
        def aux(x,y,search,board,check):
            # caso base
            if search == "":
                return True

            # si la casilla ya fue visitada, volver
            if (x,y) in check:
                return False
            # si no es ninguna casilla por limites, volver
            if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
                return False
            # si no es el caracter que buscamos, volver
            if board[y][x] != search[0]:
                return False

            # seguir buscando para search
            search = search[1:]
 
            # marcar casilla como pasada
            check.add((x,y))

            # buscar en las cuatro direcciones
            if aux(x,y+1,search,board,check):
                return True
            if aux(x,y-1,search,board,check):
                return True
            if aux(x+1,y,search,board,check):
                return True
            if aux(x-1,y,search,board,check):
                return True

            # si no se encontro nada, se limpia el conjunto de pasadas
            check.discard((x,y))

            return False
        
        for i in range(len(board[0])):
            for j in range(len(board)):
                if aux(i,j,word,board,check):
                    print(i,j)
                    return True

        return False
        