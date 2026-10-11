import math

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        output = []

        def spiral(idx):
            if idx >= len(matrix[0])-idx:
                return
            
            # explorar arriba
            for i in range(idx,len(matrix[0])-idx):
                output.append(matrix[idx][i])
                print(f"arriba agregó {matrix[idx][i]}")

            if idx+1 >= len(matrix)-idx:
                return

            # explorar derecha
            for i in range(idx+1,len(matrix)-idx):
                output.append(matrix[i][-1*(idx+1)])
                print(f"derecha agregó {matrix[i][-1*(idx+1)]}")

            # explorar abajo
            for i in range(-(idx+1)-1,-len(matrix[0])+idx-1,-1):
                output.append(matrix[-(idx+1)][i])
                print(f"abajo agregó {matrix[-(idx+1)][i]}")

            if(matrix[0][-idx-1]==matrix[0][idx]):
                return

            # explorar izq
            for i in range(-(idx+2),-len(matrix)+idx,-1):
                output.append(matrix[i][idx])
                print(f"izquierda agregó {matrix[i][idx]}")

        it = min(len(matrix),len(matrix[0]))/2
        it = math.ceil(it)
        print(f"it: {it}")
        print(range(it))
        for i in range(it):
            spiral(i)

        return output

        