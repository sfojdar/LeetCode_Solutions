# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        data=[]
        temp=head
        while temp:
            data.append(temp.val)
            temp=temp.next
        data_1=data[::-1]
        a=len(data)//2
        data_1=data_1[:a]
        data=data[:a]
        max=0
        for i in range(a):
            sum=0
            sum=data[i]+data_1[i]
            if sum>max:
                max=sum
        return max