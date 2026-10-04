class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l < r:
            added = numbers[l] + numbers[r]

            if added == target:
                return [l + 1, r + 1]
            
            if added < target:
                l += 1
            else:
                r -= 1
        
        return []