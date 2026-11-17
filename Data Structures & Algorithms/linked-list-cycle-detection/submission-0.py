# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head

        while fast and fast.next: # Fast and fast.next cannot be null since it needs to cycle

            slow = slow.next # Shift by 1 

            fast = fast.next.next # Shift by 2 

            if slow == fast: # Cycle Exists
                return True

        return False 
