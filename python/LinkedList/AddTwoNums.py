class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newhead = ListNode()
        curr = newhead
        carry = 0
      


        while l2 or l1:
            if l2 and l1:
                res = l2.val + l1.val + carry
                carry = 0
                if res >= 10:
                    carry = res//10
                    res = res - 10
                newhead.next = ListNode(res)
                newhead = newhead.next
                l2 = l2.next
                l1 = l1.next
            elif l2:
                res = l2.val + carry
                carry = 0
                if res >= 10:
                    carry = res//10
                    res =  res - 10
                newhead.next = ListNode(res)
                newhead = newhead.next
                l2 = l2.next
            else:
                res = l1.val+carry
                carry = 0
                if res >= 10:
                    carry = res//10
                    res = res - 10
                newhead.next = ListNode(res)
                newhead = newhead.next
                l1 = l1.next

        if carry > 0:
            newhead.next = ListNode(carry)
       
            
        return curr.next