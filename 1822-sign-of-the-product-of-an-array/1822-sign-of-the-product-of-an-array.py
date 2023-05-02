class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c_neg = 0
        zeros=0
        for i in nums:
            if i<0:
                c_neg+=1
            if i==0:
                zeros+=1
        if zeros !=0:
            return 0
        if c_neg %2==0:
            return 1
        else:
            return -1