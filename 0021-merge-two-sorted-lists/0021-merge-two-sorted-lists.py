# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d=n=ListNode(0)
        list=[]
        temp_1=list1
        temp_2=list2
        while temp_2 and temp_1:
            a=temp_1.val
            b=temp_2.val
            if  a<=b :
                list.append(temp_1.val)
                temp_1=temp_1.next
            else:
                list.append(temp_2.val)
                temp_2=temp_2.next
        if temp_1:
            while temp_1:
                list.append(temp_1.val)
                temp_1=temp_1.next
        if temp_2:
            while temp_2:
                list.append(temp_2.val)
                temp_2=temp_2.next
        for i in range(len(list)):
            d.next=ListNode(list[i])
            d=d.next
        return n.next