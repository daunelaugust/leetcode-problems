# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
            
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    
        res = []

        while list1 and list2:

            if  list1.val <= list2.val:
                res.append(list1.val)
                list1 = list1.next
            else:
                res.append(list2.val)
                list2 = list2.next

        if list1:
            while list1 != None:
                res.append(list1.val)
                list1 = list1.next
        elif list2:
            while list2 != None:
                res.append(list2.val)
                list2 = list2.next


        if not res:
            return None
        
        # make head of list
        head = ListNode(res[0])
        current = head
        
        # iterate through the values and create the rest of the nodes
        for value in res[1:]:
            current.next = ListNode(value)
            current = current.next
        
        
        return head
        


       



        

        