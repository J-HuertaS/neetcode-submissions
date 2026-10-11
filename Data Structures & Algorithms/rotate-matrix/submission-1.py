class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        def rotate(idx):
            for i in range(idx,len(matrix)-idx-1):
                idx_last = -1 * (idx+1)
                # arriba por derecha
                temp = matrix[i][idx_last] # guardar derecha
                matrix[i][idx_last] = matrix[idx][i] # actualizar derecha
                # derecha por abajo
                temp2 = matrix[idx_last][-1*(i+1)] # guardar abajo
                matrix[idx_last][-1*(i+1)] = temp # actualizar abajo
                # abajo por izq
                temp = matrix[-1*(i+1)][idx] # guardar izq
                matrix[-1*(i+1)][idx] = temp2 # actualizr izq 
                # izq por arriba
                matrix[idx][i] = temp


        for i in range(len(matrix)//2):
            rotate(i)
        