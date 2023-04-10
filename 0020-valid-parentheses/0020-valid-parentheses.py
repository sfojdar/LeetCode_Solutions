class Solution:
    def isValid(self, s: str) -> bool:
        dict={
        "(":")","[":"]","{":"}"
        }
        list=[]
        for i in s[:]:
            if len(s)==1 or ( i in dict.values() and len(list)==0) or len(s)%2==1:
                return( False)
            elif i in dict.keys():
                list.append(i)
                s=s.replace(i,"-",1)
            elif i in dict.values():
                a=""
                for key, value in dict.items():
                    if i == value:
                        a=key
                if list[-1]==a:
                    x=list.pop()
                    s=s.replace(i,"-",1)
                else:
                    return( False)
        if len(list)==0:
            return( True)
        else:
            return( False)