class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        x,y=0,0
        half=len(s)//2
        a=s[:half]
        b=s[half:]
        a,b=a.lower(),b.lower()
        list=['a', 'e', 'i', 'o', 'u']
        for i in range(half):
            if a[i] in list:
                x+=1
            if b[i] in list:
                y+=1
        if x==y:
            return True
        else:
            return False