class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head
        

        curr = head

        #first pass interleave nodes
        while curr:
            temp = curr.next
            curr.next = Node(curr.val, temp)
            curr = temp

        #set random pointers
        curr = head
        while curr:
            copy = curr.next
            if curr.random:
                copy.random = curr.random.next
            curr = copy.next
        
        #last past resore pointers
        curr = head
        newhead = curr.next

        while curr:
            temp1 = curr.next
            if curr.next:
                curr.next = curr.next.next
            curr = temp1


        return newhead