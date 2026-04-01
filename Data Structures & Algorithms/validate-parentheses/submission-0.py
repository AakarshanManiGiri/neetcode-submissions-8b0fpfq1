class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = { ")" : "(", "]" : "[", "}" : "{" }
        for n in s:
            if n in map:
                if stack and stack[-1] == map[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        return True if not stack else False