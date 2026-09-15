class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = []

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                combined.append(nums1[i])
                i += 1
            else:
                combined.append(nums2[j])
                j += 1
        
        combined.extend(nums1[i:])
        combined.extend(nums2[j:])

        mid = len(combined) // 2
        print(mid)

        median = combined[mid] \
            if len(combined) % 2 != 0 \
            else (combined[mid] + combined[mid-1]) / 2
        
        return median