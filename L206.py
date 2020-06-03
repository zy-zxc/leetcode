# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        q=ListNode(head.val)
        while head.next!=None:
            p=ListNode(head.next.val)
            p.next=q
            q=p
            head=head.next