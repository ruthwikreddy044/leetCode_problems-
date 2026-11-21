# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:

        if head==None or head.next==None:
            return None
        temp=head
        count=0
        while temp!=None :
            
            temp=temp.next
            count=count+1
        n=count//2 
        temp=head
        x=1
        while x<n and temp.next:

            temp=temp.next
            x=x+1
        if temp.next:
            temp.next=temp.next.next 
        else:
            temp.next=None
        return head