# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = 1
        root = head
        while root.next != None:
            root = root.next
            length += 1
        left = ListNode(0, head)
        right = left.next
        root = left
        for i in range(int(length / k)):
            value_list = []
            for j in range(k):
                value_list.append(right.val)
                right = right.next
            for j in range(k):
                left.next = ListNode(value_list.pop())
                left = left.next
            left.next = right

        return root.next
"""Space complexity is 2k while time complexity is 2k*time(pop)+3n*time(pointer), if using constant space, The solution will have a much bigger mutiplier in front of time(pointer)"""