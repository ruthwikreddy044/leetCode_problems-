# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        i=head
        dummy=None
        while i:
            N=i.next
            i.next=dummy
            dummy=i
            i=N
        return dummy    
           


         

    
        