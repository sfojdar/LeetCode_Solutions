class Solution:
    def printVertically(self, s: str) -> List[str]:
        list=s.split()
        lenght=0
        for i in list:
            if len(i)>lenght:
                lenght=len(i)
        list1=[""]*lenght
        for j in list:
            count=0
            for i in range(len(j)):
                a=list1[i]
                a+=j[i]
                list1[i]=a
                count+=1
            while count<lenght:
                list1[count%lenght]+=" "
                count+=1
        for i in range(len(list1)):
            list1[i]=list1[i].rstrip()
        return list1