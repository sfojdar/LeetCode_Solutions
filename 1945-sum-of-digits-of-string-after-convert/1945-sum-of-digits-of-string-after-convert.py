class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans=""
        answer=0
        for i in s:
            ans+=str(ord(i)-96)
        for i in range(k):
            a=0
            for j in ans:
                a+=int(j)
            answer=a
            ans=str(a)
        return answer