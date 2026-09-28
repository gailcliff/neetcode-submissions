class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.small) > len(self.large) + 1:
            largest_in_small = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, largest_in_small)
        if len(self.large) > len(self.small) + 1:
            smallest_in_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * smallest_in_large)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2
        