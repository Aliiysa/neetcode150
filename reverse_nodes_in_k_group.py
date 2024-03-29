def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next
    
        # reverse group
        prev, curr = kth.next, groupPrev.next

        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = curr.next
        
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    return dummy.next

def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr
