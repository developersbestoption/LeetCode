class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 1:
               median = nums1[len(nums1) // 2]
        else:
               mid = len(nums1) // 2
               median = (nums1[mid - 1] + nums1[mid]) / 2
       # med=(len(nums1)+1)/2
       # return nums1[int(med)-1]
        return median
a=Solution()
print(a.findMedianSortedArrays([1,2,3],[4,5,6]))