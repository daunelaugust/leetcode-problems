def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

    #following along neetcode solution

    dummy = ListNode(0,head)
    groupPrev = dummy

    while True:
        kth = self.getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        prev, curr = kth.next, groupPrev.next

        while curr != groupNext:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    
    return dummy.next






    

def getKth(self, curr, k):

    while curr and k>0:
        curr = curr.next
        k-=1
    return curr