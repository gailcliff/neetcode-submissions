class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nodes = sorted((num, i) for i, num in enumerate(nums))

        i = 0
        j = len(nums) - 1

        while i < j:
            total = nodes[i][0] + nodes[j][0]

            if total == target:
                return sorted([nodes[i][1], nodes[j][1]])
            elif total < target:
                i += 1
            elif total > target:
                j -= 1
        
        return []