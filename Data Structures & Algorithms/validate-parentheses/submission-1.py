class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        for char in s:
            if char in brackets:
                # Check that stack is nonempty and pop top element
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            # Add opening bracket
            else:
                stack.append(char)
        # Ensure that it's empty
        if not stack:
            return True
        else:
            return False
