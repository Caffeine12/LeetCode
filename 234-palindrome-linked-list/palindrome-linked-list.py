# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        count=1
        current = head
        while current.next:
            count=count+1
            current = current.next
        headOne = head
        headTwo = head
        for i in range(1,(count//2)+1):            
            if(i==count//2):
                headTwo = head.next
                head.next = None
            head = head.next
        prev = None
        while headTwo:
            next_node = headTwo.next
            headTwo.next = prev
            prev = headTwo
            headTwo = next_node
        flag = True
        for i in range(1,(count//2)+1):
            if headOne.val != prev.val:
                flag = False
            else:
                headOne = headOne.next
                prev = prev.next
        return flag
        