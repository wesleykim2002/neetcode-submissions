# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = deque([p]), deque([q])

        while q1 and q2:
            for i in range(len(q1)):
                l, r = q1.popleft(), q2.popleft()

                # checks equality and None value
                if l == None and r == None:
                    continue
                if not l or not r or not l.val == r.val:
                    return False
                q1.append(l.left)
                q2.append(r.left)
                q1.append(l.right)
                q2.append(r.right)
        return True
                