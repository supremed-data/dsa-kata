# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        slow = dummy

        left = l1
        right = l2
        temp_value = 0

        while True:
            temp_value = max(temp_value, 0)

            if left:
                temp_value += left.val
                left = left.next
            
            if right:
                temp_value += right.val
                right = right.next
            
            if temp_value >= 10:
                diff = temp_value - 10
                temp_value = 1
            else:
                diff = temp_value
                temp_value = 0

            slow.next = ListNode(diff)
            slow = slow.next

            if left or right:
                continue
            else:
                if temp_value == 1:
                    slow.next = ListNode(temp_value)
                    slow = slow.next
                break

        return dummy.next
