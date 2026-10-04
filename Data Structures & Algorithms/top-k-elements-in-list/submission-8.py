class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)

        nlargest = heapq.nlargest(
            k, 
            counter.items(), 
            key=lambda item: item[1]
        )

        return [item[0] for item in nlargest]
