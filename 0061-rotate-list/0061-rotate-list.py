# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        counter=0
        temp_2=head
        while temp_2:
            counter+=1
            temp_2=temp_2.next
        for i in range(k%counter):
            temp=head
            temp_1=head
            while temp.next:
                temp=temp.next
            while temp_1.next.next:
                temp_1=temp_1.next
            temp.next=head
            temp_1.next=None
            head=temp    
        return head    