class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        min_rate = r

        while l <= r:
            k = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                # find better
                min_rate = k
                r = k - 1
            else:
                l = k + 1
        
        return min_rate

