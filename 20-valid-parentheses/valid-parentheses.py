class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeTOopen = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in closeTOopen:
                if not stack:
                    return False
                top = stack.pop()

                if closeTOopen[i] != top:
                    return False
            else:
                stack.append(i)

        return not stack