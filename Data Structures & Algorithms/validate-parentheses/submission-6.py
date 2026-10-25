class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = ['(', '{', '[']
        closed_brackets = [')', '}', ']']

        for bracket in s:
            if bracket in closed_brackets:
                if stack and brackets[closed_brackets.index(bracket)] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        if stack:
            return False
        else:
            return True