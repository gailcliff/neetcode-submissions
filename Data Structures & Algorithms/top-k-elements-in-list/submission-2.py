class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        count_pairs = list(counts.items())
        count_pairs.sort(key=lambda item: -item[1])

        topk = [count_pairs[i][0] for i in range(k)]

        return topk

        