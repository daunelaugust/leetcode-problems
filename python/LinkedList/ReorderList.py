def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # get mid point
    slow,fast = head, head.next

    while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

    # make two seperate list for the first set end to null
    second = slow.next
    rev = slow.next = None

    #reverse the second
    while second:
        temp = second.next
        second.next = rev
        rev = second
        second = temp

    first, second = head, rev

    #merge the lists
    while second:
        # store the next variable of both pointers
        temp1,temp2 = first.next, second.next
        # store the second half pointer as the next item for the first half pointer
        first.next = second
        #store the next variable for the second half pointer as the what would be next for first
        second.next = temp1
        #skip to the next elements for both halfs which is what is in the temps
        first, second = temp1, temp2