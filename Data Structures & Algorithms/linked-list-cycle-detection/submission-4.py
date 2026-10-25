# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []

        cur = head.next

        while cur:
            if cur in visited:
                return True
            else:
                visited.append(cur)
                cur = cur.next

        return False