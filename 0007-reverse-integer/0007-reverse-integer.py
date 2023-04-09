class Solution:
    def reverse(self, x: int) -> int:
        a=str(abs(x))
        a=a[::-1]
        ans=0
        for i in a:
            ans=ans*10+int(i)
        if x<0:
            ans*=-1
        if ans>(2**31)-1 or ans<(-2**31):
            return 0
        else:
            return ans


        