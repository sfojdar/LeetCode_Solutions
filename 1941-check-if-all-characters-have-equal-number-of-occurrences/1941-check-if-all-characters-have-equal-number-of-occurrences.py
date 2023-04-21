class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        ans1=[]
        ans2=[]
        for i in s:
            if i not in ans1:
                ans1.append(i)
                ans2.append(0)
            else:
                a=ans1.index(i)
                ans2[a]+=1
        x=ans2[0]
        for i in ans2:
            if i==x:
                continue
            else:
                return False
        return True