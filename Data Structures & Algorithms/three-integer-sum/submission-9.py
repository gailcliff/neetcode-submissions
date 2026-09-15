class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triples = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            m = i + 1
            n = len(nums) - 1

            while m < n:
                total = nums[i] + nums[m] + nums[n]
                if total < 0:
                    m += 1
                elif total > 0:
                    n -= 1
                else:
                    triples.append([nums[i], nums[m], nums[n]])
                    
                    m += 1
                    n -= 1

                    while m < n and nums[m] == nums[m-1]:
                        m += 1
                    
                    while m < n and nums[n] == nums[n+1]:
                        n -= 1
            
        return triples