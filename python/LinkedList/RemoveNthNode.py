# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None


        curr = head
        count1 = count2 =  0

        while curr:
            count1+=1
            curr = curr.next

        if count1 == 1 and n:
            return None
        
        if n == count1:
            return head.next

        prev, curr = head, head.next
        
        while curr:
            count2+=1

            if curr and count1-n == count2:
                prev.next = curr.next
                
                break
            curr = curr.next
            prev = prev.next
            
        return head
        