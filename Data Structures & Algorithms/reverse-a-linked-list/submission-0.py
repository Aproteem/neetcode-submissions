# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        else:
            prevnode = None
            thisnode = head
            nextnode = head.next
            while thisnode != None:
                thisnode.next = prevnode
                #update nodes
                prevnode = thisnode
                thisnode = nextnode
                if(nextnode):
                    nextnode = nextnode.next
            return prevnode



            

 

