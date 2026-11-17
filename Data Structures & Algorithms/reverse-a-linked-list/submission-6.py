# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        prev, curr = None, head

        while curr:

            t = curr.next # eventually this will point to a null value, which is assigned to curr, therefore curr will be false and the while loop will stop 
            curr.next = prev
            prev = curr # at the end prev will be representing the last node, since it will be set to curr and curr will be curr.next 
            curr = t 
     
        return prev # after curr is null it ends meaning prev will be valid


        