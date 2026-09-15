class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # seen = {}

        # for i, num in enumerate(numbers):
        #     i += 1
        #     complement = target - num

        #     if complement in seen:
        #         return [seen[complement], i]
            
        #     seen[num] = i
        
        # return []

        i = 0
        j = len(numbers) - 1

        while i < j:
            total = numbers[i] + numbers[j]

            if total < target:
                i += 1
            elif total > target:
                j -= 1
            else:
                return [i+1, j+1]
        
        return []