class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        if len(nums)==0 or (target not in nums):
            return(ans)
        if len(nums)==1:
            return( [0,0])
        for i in range(len(nums)):
            if nums[i]==target:
                ans[0]=i
                break
        for i in range(ans[0],len(nums)):
            if i==len(nums)-1 and nums[i]==target:
                ans[1]=i
                return ans
            if nums[i]!=target:
                ans[1]=i-1
                return(ans)
