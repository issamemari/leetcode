import heapq


class MedianFinder:
    def __init__(self):
        self.leftHeap, self.rightHeap = [], []

    def addNum(self, num: int) -> None:
        if self.leftHeap and num > -self.leftHeap[0]:
            if self.rightHeap and num < self.rightHeap[0]:
                if len(self.leftHeap) <= len(self.rightHeap):
                    heapq.heappush(self.leftHeap, -num)
                else:
                    heapq.heappush(self.rightHeap, num)
            else:
                if len(self.leftHeap) <= len(self.rightHeap):
                    heapq.heappush(self.leftHeap, -heapq.heappop(self.rightHeap))
                heapq.heappush(self.rightHeap, num)
        else:
            if len(self.leftHeap) > len(self.rightHeap):
                heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))
            heapq.heappush(self.leftHeap, -num)

    def findMedian(self) -> float:
        if len(self.leftHeap) == len(self.rightHeap):
            return (self.rightHeap[0] - self.leftHeap[0]) / 2

        return -self.leftHeap[0]
