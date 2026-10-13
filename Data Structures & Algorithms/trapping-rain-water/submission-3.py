class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]

        # obtener maximos a la izquierda
        temp_max = 0
        for i in range(len(height)):
            left[i] = temp_max
            temp_max = max(temp_max,height[i])
        # obtener maximos a la derecha
        temp_max = 0
        for i in range(len(height)-1,-1,-1):
            right[i] = temp_max
            temp_max = max(temp_max,height[i])

        output = 0
        for i in range(len(height)):
            output += max(0,min(left[i],right[i]) - height[i])


        return output


        