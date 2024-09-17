class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        cycleSet = set()

        curr = head

        if not head:
            return False


        while curr:
            if cycleSet and curr in cycleSet:
                return True
            cycleSet.add(curr)
            curr = curr.next

        return False


# can do better with 0(1) memory using fast and slow pointer