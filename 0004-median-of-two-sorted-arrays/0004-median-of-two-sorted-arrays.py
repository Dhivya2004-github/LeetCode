class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge=nums1 + nums2
        merge.sort()
        n=len(merge)
        if n%2==0:
            v=n//2
            median=(merge[v]+merge[v-1])/2.0
        else:
            median=merge[n//2]
        return median