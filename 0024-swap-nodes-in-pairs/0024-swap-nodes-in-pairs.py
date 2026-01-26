# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        cum_sum = 0

        while current and current.next:
            if cum_sum % 2 == 0:
                front, back = current, current.next
                temp = front.val
                front.val = back.val
                back.val = temp

            current = current.next
            cum_sum += 1

        return head
