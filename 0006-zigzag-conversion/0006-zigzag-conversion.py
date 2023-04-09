class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans=[]
        n=numRows
        answer=""
        counter=1
        if len(s)<=numRows:
            return s 
        if numRows==1:
            return s
        if numRows==2:
            q="" 
            p=""  
            for i in range(len(s)):
                if i%2==0:
                    q+=s[i]
                else:
                    p+=s[i]
            return q+p
        while len(s)!=0:
            if counter==1:
                a=s[:n]
                q=[i for i in a]
                if len(q)!=numRows:
                    for i in range(numRows-len(q)):
                        q.append("_")
                ans.append(q)
                s=s[n:]
                counter+=1
            elif counter!=numRows-1:
                x=['_']*n
                a=s[0]
                s=s[1:]
                x[(-counter)]=a
                ans.append(x)
                counter+=1
            elif counter==numRows-1:
                x=['_']*n
                a=s[0]
                s=s[1:]
                x[(-counter)]=a
                ans.append(x)
                counter=1
        for i in range(numRows):
            for j in ans:
                answer+=j[i]
        answer=answer.replace("_","")
        return( answer)
            
