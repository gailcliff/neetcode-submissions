class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # if nums[mid] > nums[r], it means the left portion of
                # the list is the fully sorted portion and therefore the
                # minimum element must be on the right of mid
                l = mid + 1
            else:
                # if nums[mid] < nums[r], it means that the right portion
                # of the list is the fully sorted portion, and therefore
                # the minimum must be on the left side (and it might)
                # even be at mid, so we set right = mid
                r = mid
            # as we reduce the scope of where to look at, we must make sure
            # that at least one side of the list contains items that are
            # out of order and the other side contains items that are
            # fully in order, until 
        
        return nums[r]