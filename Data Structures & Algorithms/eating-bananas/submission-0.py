class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_rate = float('inf')

        while l <= r:
            candidate_rate = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / candidate_rate)
            
            if hours <= h:
                min_rate = min(min_rate, candidate_rate)
                r = candidate_rate - 1
                print(candidate_rate)
            else:
                l = candidate_rate + 1
        
        return min_rate