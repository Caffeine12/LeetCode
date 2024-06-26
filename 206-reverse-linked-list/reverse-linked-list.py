# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        else:
            new_node = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return new_node