class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            a=str(i)
            for j in a:
                ans.append(int(j))
        return ans