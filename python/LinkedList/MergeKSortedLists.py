class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            #temporarily holds lists
            res = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                res.append(self.mergeTwoLists(l1,l2))
            lists = res
        return lists[0]




    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode()
        head = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next
            
        if list1:
            dummy.next = list1
        else:
            dummy.next = list2
        

        return head.next