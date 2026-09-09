import heapq

class MedianFinder:

    def __init__(self):
        self.data1 = []
        self.data2 = []
        self.mid = 0
        

    def addNum(self, num: int) -> None:
        if num <= self.mid:
            heapq.heappush(self.data1,-num)
        else:
            heapq.heappush(self.data2,num)

        # ahora, si hay desbalance
        # desbalance de menor cantidad "abajo" de mid
        while len(self.data2) > len(self.data1) + 1:
            temp = -heapq.heappop(self.data2)
            heapq.heappush(self.data1,temp)
        # desbalance de menor cantidad "arriba" de mid
        while len(self.data1) > len(self.data2) + 1:
            temp = -heapq.heappop(self.data1)
            heapq.heappush(self.data2,temp)
        if len(self.data1):
            self.mid = -self.data1[0]
            

        

    def findMedian(self) -> float:
        if (len(self.data1)+len(self.data2))%2: # si hay impares
            if len(self.data1) > len(self.data2):
                return self.data1[0]*-1
            return self.data2[0]

        return (self.data2[0] + self.data1[0] * -1)/2
        
        