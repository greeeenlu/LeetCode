# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = temp = ListNode(None)
        summary = 0
        while l1 or l2 or summary:
            if l1:
                summary += l1.val
                l1 = l1.next
            if l2:
                summary += l2.val
                l2 = l2.next

            temp.next = ListNode(summary % 10)
            temp = temp.next
            summary = summary // 10

        return result.next