# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        prev_node = None
        cur_node, next_node = head, head

        while next_node:
            next_node = next_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        return prev_node
