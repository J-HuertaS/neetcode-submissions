import heapq

class MedianFinder:

    def __init__(self):
        self.data1 = []
        self.data2 = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.data1,-num)

        # SI EL MAXIMO DE DATA1 ES MAYOR QUE EL MINIMO DE DATA2, ACTUALIZAR
        if self.data2 and self.data1[0]*-1 > self.data2[0]:
            heapq.heappush(self.data2,-heapq.heappop(self.data1))

        # AHORA SI, REVISAR SIZES
        if len(self.data1) > len(self.data2) + 1:
            heapq.heappush(self.data2,-heapq.heappop(self.data1))
        elif len(self.data2) > len(self.data1):
            heapq.heappush(self.data1,-heapq.heappop(self.data2))

    def findMedian(self) -> int:
        if (len(self.data1) + len(self.data2)) % 2:
            return self.data1[0]*-1
        
        return (self.data1[0]*-1+self.data2[0])/2
        
        