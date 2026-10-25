class Solution:
    def isValid(self, s: str) -> bool:
        closingBrackets = [')', ']', '}']
        openingBrackets = ['(', '[', '{']

        stack = []

        for bracket in s:
            if bracket in closingBrackets:
                if stack and openingBrackets[closingBrackets.index(bracket)] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        if stack:
            return False
        else:
            return True