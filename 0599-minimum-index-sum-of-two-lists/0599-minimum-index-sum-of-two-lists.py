class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[]
        count=len(list1)+len(list2)
        for i in list1:
            b=list1.index(i)
            if i in list2:
                a=list2.index(i)
                if a+b==count:
                    count=a+b
                    ans.append(i)
                if a+b<count:
                    count=a+b
                    ans=[]
                    ans.append(i)
        return ans