class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1+nums2
        a.sort()
        if len(a)%2==0:
            x=len(a)//2-1
            y=x+1
            median=(a[x]+a[y])/2
        else:
            s=len(a)//2
            median=a[s]
        return median