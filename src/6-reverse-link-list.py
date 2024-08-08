from typing import Optional

# definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# iterative solution. complexity O(n)        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head # use two pointers

        while curr:
            nxt = curr.next # save the next node
            curr.next = prev # reverse the current node
            prev = curr # move the pointers
            curr = nxt # move the pointers

        return prev
